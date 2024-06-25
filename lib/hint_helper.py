import re
from discord import Embed, Color

with open('data/pokes/pokemon', 'r', encoding='utf8') as file:
  pokemon_list = file.read()


def solve(message):
  hint = []
  for i in range(15, len(message) - 1):
    if message[i] != '\\':
      hint.append(message[i])
  hint_string = ''
  for i in hint:
    hint_string += i
  hint_replaced = hint_string.replace('_', '.')
  solution = re.findall('^' + hint_replaced + '$', pokemon_list, re.MULTILINE)
  return solution

async def hint_embed(i, message):
  embed = Embed(title='Hint solved!', color=Color.blue())
  embed.set_footer(text="❤️ The OutN Project")
  embed.add_field(name=f'The Pokemon is {i}', value=message.content)
  embed.add_field(name='Command', value=f"@Pokétwo#8236 c {i}")
  await message.channel.send(embed=embed)

