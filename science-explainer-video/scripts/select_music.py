"""Select an available approved music master from a local catalog (stdlib only)."""
import argparse
import hashlib
import json
from pathlib import Path


def resolve_catalog(explicit):
    if explicit:
        return Path(explicit).expanduser().resolve()
    owner_config = Path(__file__).resolve().parents[1] / 'references' / 'owner-music-library.json'
    if not owner_config.is_file():
        raise ValueError('No local music catalog configured; supply --catalog or configure owner-music-library.json.')
    config = json.loads(owner_config.read_text(encoding='utf-8-sig'))
    return Path(config['catalog']).expanduser().resolve()


def check_track(track, root):
    if not track.get('auto_eligible') or track.get('asset_kind') != 'full_master':
        return None, 'not enabled as a full master'
    if track.get('rights', {}).get('status') not in {'cc_by_4_0_attribution', 'cc_by_3_0_attribution', 'owner_approved'}:
        return None, 'video-use conditions unresolved'
    asset = track.get('asset') or {}
    if not asset.get('path') or not asset.get('decode_verified') or not asset.get('sha256'):
        return None, 'asset verification missing'
    path = Path(asset['path'])
    path = path if path.is_absolute() else root / path
    if not path.is_file():
        return None, 'asset file missing'
    if path.stat().st_size != asset.get('bytes'):
        return None, 'asset size changed'
    digest = hashlib.sha256()
    with path.open('rb') as source:
        for block in iter(lambda: source.read(1024 * 1024), b''):
            digest.update(block)
    if digest.hexdigest().lower() != asset['sha256'].lower():
        return None, 'asset checksum changed'
    return str(path.resolve()), None


def choose(catalog, root, topic, mode, requested=None):
    text = topic.casefold()
    categories = [rule['category'] for rule in catalog.get('topic_rules', [])
                  if any(word.casefold() in text for word in rule['keywords'])]
    if not categories:
        categories = ['general']
    preferences = catalog['category_preferences']
    available, excluded = [], []
    for track in catalog['tracks']:
        path, error = check_track(track, root)
        if error:
            excluded.append({'id': track['id'], 'reason': error})
            continue
        if requested and track['id'] != requested:
            continue
        scores = [100 - 10 * preferences[category].index(track['id'])
                  for category in categories if track['id'] in preferences.get(category, [])]
        score = (max(scores) if scores else 0) + track.get('mode_scores', {}).get(mode, 0)
        available.append((score, track['id'], track, path))
    if not available:
        raise ValueError('No verified usable master matches this request. Restore the chosen asset or resolve its conditions; do not use a preview or silently replace an explicit request.')
    score, _, track, path = sorted(available, key=lambda row: (-row[0], row[1]))[0]
    return {
        'selection': track['id'], 'title': track['title'], 'artist': track['artist'],
        'version': track['version'], 'asset': path, 'sha256': track['asset']['sha256'],
        'duration_seconds': track['asset']['duration_seconds'],
        'topic_categories': categories, 'mode': mode, 'score': score,
        'reason': track.get('fit', ''), 'source': track['source'],
        'credit_for_description': track['rights'].get('credit', ''),
        'usage_conditions': track['rights'].get('conditions', ''),
        'mixing_note': 'One continuous bed; use clean musical joins and fades. Duck music under narration. Listen to final edits; do not change reading holds just to hit a beat.',
        'excluded': excluded,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--catalog', help='Local catalog JSON; defaults to installation owner config.')
    parser.add_argument('--topic', default='', help='Topic plus desired mood and content structure.')
    parser.add_argument('--mode', choices=('minimalist', 'narrated'), default='minimalist')
    parser.add_argument('--track-id', help='Explicit user choice; never substitutes a different track.')
    parser.add_argument('--silent', action='store_true', help='Explicit silent / owner-adds-music request.')
    args = parser.parse_args()
    if args.silent:
        result = {'selection': None, 'audio_stream': False, 'reason': 'Explicit silent / owner-adds-music brief.'}
    else:
        try:
            catalog_path = resolve_catalog(args.catalog)
            catalog = json.loads(catalog_path.read_text(encoding='utf-8-sig'))
            result = choose(catalog, catalog_path.parent, args.topic, args.mode, args.track_id)
        except (ValueError, KeyError, OSError) as error:
            parser.exit(2, f'Music selection unavailable: {error}\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
