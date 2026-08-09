from discord import Embed

from constants import COLOR_COMMON, FOOTER

HINT_PREFIX = 'The pokémon is '

with open('data/pokes/pokemon', 'r', encoding='utf8') as file:
  pokemon_list = [line.strip() for line in file if line.strip()]


def extract_hint(content):
  """Pull the masked name out of a Poketwo hint message.

  Poketwo escapes the blanks as '\\_' and ends the sentence with punctuation.
  Returns '' when the message isn't actually a hint.
  """
  _, sep, rest = content.partition(HINT_PREFIX)
  if not sep:
    return ''
  return rest.replace('\\', '').strip().rstrip('.').strip().lower()


def solve(content):
  """Return every Pokémon matching the hint, '_' being a single wildcard char.

  Deliberately not regex: this runs on messages from arbitrary users, so
  feeding their text to `re` invites catastrophic backtracking.
  """
  hint = extract_hint(content)
  if not hint:
    return []

  return [name for name in pokemon_list
          if len(name) == len(hint)
          and all(h == '_' or h == n for h, n in zip(hint, name))]


async def hint_embed(i, message):
  embed = Embed(title='Hint solved!', color=COLOR_COMMON)
  embed.set_footer(text=FOOTER)
  embed.add_field(name=f'The Pokemon is {i}', value=message.content)
  embed.add_field(name='Command', value=f"@Pokétwo#8236 c {i}")
  await message.channel.send(embed=embed)
