import configparser
import os

CONFIG_FILE = 'config.ini'

_PROMPTS = [
    # (key, question, id_prompt)
    ('RPING', "Do you want rare ping (y/n): ", "Enter the role ID for rare ping: "),
    ('REGPING', "Do you want regional ping (y/n): ", "Enter the role ID for regional ping: "),
    ('STARCH', "Do you want Starboard (y/n): ", "Enter the channel ID for starboard: "),
    ('CLOG', "Do you want catch logging (y/n): ", "Enter the channel ID for Catch log: "),
    ('SPAWNLOG', "Do you want to log the spawns (y/n): ", "Enter the channel ID for Spawn log: "),
]

config = configparser.ConfigParser()


def _is_yes(answer):
  """Empty string is NOT a yes. `'' in 'Yy'` is True, which is the bug this avoids."""
  return answer.strip().upper().startswith('Y')


def create_config():
  """Prompt the user and write config.ini. Only called when the file is absent."""
  token = input("Enter your Discord bot token: ")
  confirms, values = {}, {'TOKEN': token}

  for key, question, id_prompt in _PROMPTS:
    answer = input(question)
    confirms[key + 'CONFIRM'] = answer
    values[key] = input(id_prompt) if _is_yes(answer) else ''

  config['CONFIRMS'] = confirms
  config['DEFAULT'] = values
  with open(CONFIG_FILE, 'w') as configfile:
    config.write(configfile)


def get_config():
  if not os.path.exists(CONFIG_FILE):
    create_config()
  config.read(CONFIG_FILE)


get_config()


def _channel(key):
  raw = config['DEFAULT'].get(key, '')
  return int(raw) if raw.strip() else None


TKN = config['DEFAULT']['TOKEN']

rping = _channel('RPING')
regping = _channel('REGPING')
starch = _channel('STARCH')
clog = _channel('CLOG')
spawnlog = _channel('SPAWNLOG')

# A feature is on only if the user said yes AND gave a usable ID.
rpingconfirm = _is_yes(config['CONFIRMS'].get('RPINGCONFIRM', '')) and rping is not None
regpingconfirm = _is_yes(config['CONFIRMS'].get('REGPINGCONFIRM', '')) and regping is not None
starchconfirm = _is_yes(config['CONFIRMS'].get('STARCHCONFIRM', '')) and starch is not None
clogconfirm = _is_yes(config['CONFIRMS'].get('CLOGCONFIRM', '')) and clog is not None
spawnlogconfirm = _is_yes(config['CONFIRMS'].get('SPAWNLOGCONFIRM', '')) and spawnlog is not None
