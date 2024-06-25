from discord import Embed, Color
import configparser


#config
config = configparser.ConfigParser()
config_file = 'config.ini'
config.read(config_file)

rping = int(config['DEFAULT']['RPING'])
regping = int(config['DEFAULT']['REGPING'])

rpingconfirm = config['CONFIRMS']['RPINGCONFIRM']
regpingconfirm = config['CONFIRMS']['REGPINGCONFIRM']

#embeds
async def mythic_embed(message, name):
  embed = Embed(color=Color.gold())
  embed.set_footer(text="❤️ The OutN Project")
  embed.add_field(
      name='New Spawn!',
      value=f'**__{name}__**, A mythic Pokemon spawned! catch it using:')
  embed.add_field(name='Command', value=f"@Pokétwo#8236 c {name}")
  await message.channel.send(embed=embed)
  if rpingconfirm in 'Yy':
    await message.channel.send(f"<@&{rping}>")


async def legendary_embed(message, name):
  embed = Embed(color=Color.gold())
  embed.set_footer(text="❤️ The OutN Project")
  embed.add_field(
      name='New Spawn!',
      value=f'**__{name}__**, A legendary Pokemon spawned! catch it using:')
  embed.add_field(name='Command', value=f"@Pokétwo#8236 c {name}")
  await message.channel.send(embed=embed)
  if rpingconfirm in 'Yy':
    await message.channel.send(f"<@&{rping}>")


async def ub_embed(message, name):
  embed = Embed(color=Color.gold())
  embed.set_footer(text="❤️ The OutN Project")
  embed.add_field(
      name='New Spawn!',
      value=f'**__{name}__**, An Ultra Beast spawned! catch it using:')
  embed.add_field(name='Command', value=f"@Pokétwo#8236 c {name}")
  await message.channel.send(embed=embed)
  if rpingconfirm in 'Yy':
    await message.channel.send(f"<@&{rping}>")


async def reg_embed(message, name):
  embed = Embed(color=Color.yellow())
  embed.set_footer(text="❤️ The OutN Project")
  embed.add_field(
      name='New Spawn!',
      value=f'**__{name}__**, A regional Pokémon spawned! catch it using:')
  embed.add_field(name='Command', value=f"@Pokétwo#8236 c {name}")
  await message.channel.send(embed=embed)
  if regpingconfirm in 'Yy':
    await message.channel.send(f"<@&{regping}>")


async def common_embed(message, name):
  embed = Embed(color=Color.blue())
  embed.set_footer(text="❤️ The OutN Project")
  embed.add_field(name='New Spawn!',
                  value=f'**__{name}__** spawned! catch it using:')
  embed.add_field(name='Command', value=f"@Pokétwo#8236 c {name}")
  await message.channel.send(embed=embed)


