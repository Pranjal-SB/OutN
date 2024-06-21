import configparser
import os

#user inputs
config = configparser.ConfigParser()
config_file = 'config.ini'

def get_config():
  if not os.path.exists(config_file):
    token = input("Enter your Discord bot token: ")
    rping = input("Enter the role ID for rare ping: ")
    regping = input("Enter the role ID for regional ping: ")
    config['DEFAULT'] = {'TOKEN': token, 'RPING': rping, 'REGPING': regping}

    with open(config_file, 'w') as configfile:
      config.write(configfile)
  else:
    config.read(config_file)

get_config()

TKN = config['DEFAULT']['TOKEN']
rping = int(config['DEFAULT']['RPING'])
regping = int(config['DEFAULT']['REGPING'])
