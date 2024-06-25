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

        config['CONFIRMS'] = {'RPINGCONFIRM': rpingconfirm, 'REGPINGCONFIRM': regpingconfirm, 'STARCHCONFIRM': starchconfirm, 'CLOGCONFIRM': clogconfirm}
        config['DEFAULT'] = {'TOKEN': token, 'RPING': rping, 'REGPING': regping, 'STARCH': starch, 'CLOG': clog}

        with open(config_file, 'w') as configfile:
            config.write(configfile)
    else:
        config.read(config_file)

get_config()


TKN = config['DEFAULT']['TOKEN']
rping = int(config['DEFAULT']['RPING'])
regping = int(config['DEFAULT']['REGPING'])
starch = int(config['DEFAULT']['STARCH'])
clog = int(config['DEFAULT']['CLOG'])
