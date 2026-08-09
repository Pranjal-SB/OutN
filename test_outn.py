"""Self-check for the two things that silently broke spawns before.

Run from the repo root: `python test_outn.py`

Needs no third-party packages: discord is stubbed so the pure logic can be
checked without installing tensorflow.
"""

import json
import sys
import types

sys.path.insert(0, 'lib')

# Minimal discord stub. constants.py and hint_helper.py only need Embed/Color.
_discord = types.ModuleType('discord')


class _Color:
  def __init__(self, value):
    self.value = value

  @classmethod
  def gold(cls):
    return cls(0xf1c40f)

  @classmethod
  def blue(cls):
    return cls(0x3498db)


_discord.Color = _Color
_discord.Embed = object
sys.modules.setdefault('discord', _discord)

import hint_helper  # noqa: E402
import pokedex  # noqa: E402


def test_tier_files_only_contain_real_class_names():
  """Data drift is what made 'ting-Lu' and '10% zygarde' unreachable."""
  classes = set(json.load(open('data/classes.json', encoding='utf8')))
  for label, names in [('mythical', pokedex.MYTHICAL),
                       ('legendary', pokedex.LEGENDARY),
                       ('ultrabeast', pokedex.ULTRA_BEAST),
                       ('regional', pokedex.REGIONAL)]:
    unknown = sorted(names - classes)
    assert not unknown, f"{label} lists names the model can never predict: {unknown}"


def test_every_class_is_tierable():
  for name in pokedex.classes:
    assert pokedex.tier_of(name) in {'mythic', 'legendary', 'ub', 'regional', 'common'}


def test_index_lookup_round_trips():
  for name, index in pokedex.classes.items():
    assert pokedex.index_to_name[index] == name


def test_known_tiers():
  cases = {
      'mew': 'mythic',
      'deoxys-normal': 'mythic',
      'mewtwo': 'legendary',
      'articuno galar': 'legendary',   # was 'regional' (list said 'articuno-galar')
      'ting-lu': 'legendary',          # was 'common' (list said 'ting-Lu')
      'zygarde-10': 'legendary',       # was 'common' (list said '10% zygarde')
      'zygarde-50': 'legendary',       # was 'common'
      'eternatus': 'legendary',
      'natu': 'common',                # substring of 'eternatus'; needed a hack before
      'nihilego': 'ub',
      'meowth-galar': 'regional',
      'obstagoon': 'regional',
      'bulbasaur': 'common',
  }
  for name, expected in cases.items():
    assert name in pokedex.classes, f"{name} is not a model class"
    got = pokedex.tier_of(name)
    assert got == expected, f"{name}: expected {expected}, got {got}"


def test_hint_solving():
  assert hint_helper.solve('The pokémon is p\\_k\\_chu.') == ['pikachu']
  assert 'mew' in hint_helper.solve('The pokémon is \\_\\_\\_.')
  assert hint_helper.solve('The pokémon is \\_\\_\\_.') == \
      [n for n in hint_helper.pokemon_list if len(n) == 3]
  assert hint_helper.solve('hello there') == []


def test_hint_input_is_not_a_regex():
  """User-controlled text used to be compiled as a pattern."""
  assert hint_helper.solve('The pokémon is (a+)+b') == []
  assert hint_helper.solve('The pokémon is .*') == []


if __name__ == '__main__':
  failures = 0
  for name, fn in sorted(globals().items()):
    if not name.startswith('test_'):
      continue
    try:
      fn()
      print(f"PASS {name}")
    except AssertionError as exc:
      failures += 1
      print(f"FAIL {name}: {exc}")
  print(f"\n{failures} failure(s)")
  sys.exit(1 if failures else 0)
