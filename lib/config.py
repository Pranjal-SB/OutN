import configparser
import os

# user inputs
config = configparser.ConfigParser()
config_file = 'config.ini'


def get_config():
    if not os.path.exists(config_file):
        token = input("Enter your Discord bot token: ")

        rping = ''
        rpingconfirm = input("Do you want rare ping (y/n): ")
        if rpingconfirm in "Yy":
            rping = input("Enter the role ID for rare ping: ")

        regping = ''
        regpingconfirm = input("Do you want regional ping (y/n): ")
        if regpingconfirm in "Yy":
            regping = input("Enter the role ID for regional ping: ")

        starch = ''
        starchconfirm = input("Do you want Starboard (y/n): ")
        if starchconfirm in "Yy":
            starch = input("Enter the channel ID for starboard: ")

        clog = ''
        clogconfirm = input("Do you want catch logging (y/n): ")
        if clogconfirm in "Yy":
            clog = input("Enter the channel ID for Catch log: ")

        spawnlog = ''
        spawnlogconfirm = input("Do you want to log the spawns (y/n): ")
        if spawnlogconfirm in "Yy":
            spawnlog = input("Enter the channel ID for Spawn log: ")

        config['CONFIRMS'] = {
            'RPINGCONFIRM': rpingconfirm, 'REGPINGCONFIRM': regpingconfirm, 'STARCHCONFIRM': starchconfirm, 'CLOGCONFIRM': clogconfirm, 'SPAWNLOGCONFIRM': spawnlogconfirm
        }

        config['DEFAULT'] = {'TOKEN': token, 'RPING': rping, 'REGPING': regping,
                             'STARCH': starch, 'CLOG': clog, 'SPAWNLOG': spawnlog}

        with open(config_file, 'w') as configfile:
            config.write(configfile)
    else:
        config.read(config_file)


get_config()

config.read(config_file)

# variables

TKN = config['DEFAULT']['TOKEN']

rpingconfirm = config['CONFIRMS']['RPINGCONFIRM']
regpingconfirm = config['CONFIRMS']['REGPINGCONFIRM']
starchconfirm = config['CONFIRMS']['STARCHCONFIRM']
clogconfirm = config['CONFIRMS']['CLOGCONFIRM']
spawnlogconfirm = config['CONFIRMS']['SPAWNLOGCONFIRM']

rping = int(config['DEFAULT']['RPING']) if config['DEFAULT']['RPING'] else None
regping = int(config['DEFAULT']['REGPING']
              ) if config['DEFAULT']['REGPING'] else None
starch = int(config['DEFAULT']['STARCH']
             ) if config['DEFAULT']['STARCH'] else None
clog = int(config['DEFAULT']['CLOG']) if config['DEFAULT']['CLOG'] else None
spawnlog = int(config['DEFAULT']['SPAWNLOG']
               ) if config['DEFAULT']['SPAWNLOG'] else None
