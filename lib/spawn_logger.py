from discord import Color, Embed
import configparser

# config
config = configparser.ConfigParser()
config_file = 'config.ini'
config.read(config_file)

spawnlog = int(config['DEFAULT']['SPAWNLOG'])


async def logthespawn(bot, message, name):
  splog = bot.get_channel(spawnlog)
  embed = Embed(color=Color.green())
  embed.set_footer(text="❤️ The OutN Project")
  embed.add_field(name='A pokemon spawned!', value=f'**__{name}__** spawned!')
  embed.add_field(name='Message Link', value=f'[Jump to Message]({message.jump_url})')
  await splog.send(embed=embed)
