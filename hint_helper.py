import re

with open('data/pokemon', 'r', encoding='utf8') as file:
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
