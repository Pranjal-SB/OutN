from discord import Color, Embed
import configparser

#config
config = configparser.ConfigParser()
config_file = 'config.ini'
config.read(config_file)

spawnlog = config['DEFAULT']['SPAWNLOG']

async def logthespawn(bot, message, name):
  splog = bot.get_channel(spawnlog)
  logit = Embed(color=Color.green())
  logit.set_footer(text="OutN Bot ❤️ BSBP ️")
  logit.add_field(name='A pokemon spawned!', value=f'**__{name}__** spawned!')
  logit.add_field(name='Message Link',
                  value=f'[Jump to Message]({message.jump_url})')
  await splog.send(embed=logit)
