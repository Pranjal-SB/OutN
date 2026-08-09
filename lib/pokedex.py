"""Tier lookup.

The tier files are exact-match sets, not substring blobs. Substring matching is
how 'eternatus' used to register as legendary (it contains 'natu').
"""

import json

REGIONAL_MARKERS = ('galar', 'alola', 'hisui')


def _load_set(path):
  with open(path, 'r', encoding='utf8') as f:
    return {line.strip() for line in f if line.strip()}


with open('data/classes.json', 'r', encoding='utf8') as f:
  classes = json.load(f)

# Invert once. Indexing list(classes.keys()) per prediction rebuilt 1081 entries
# each time and silently assumed dict order matched the stored indices.
index_to_name = {index: name for name, index in classes.items()}

MYTHICAL = _load_set('data/pokes/mythical')
LEGENDARY = _load_set('data/pokes/legendary')
ULTRA_BEAST = _load_set('data/pokes/ultrabeast')
REGIONAL = _load_set('data/pokes/regional')


def tier_of(name):
  """Return one of: 'mythic', 'legendary', 'ub', 'regional', 'common'."""
  if name in MYTHICAL:
    return 'mythic'
  if name in LEGENDARY:
    return 'legendary'
  if name in ULTRA_BEAST:
    return 'ub'
  if name in REGIONAL or any(m in name for m in REGIONAL_MARKERS):
    return 'regional'
  return 'common'
