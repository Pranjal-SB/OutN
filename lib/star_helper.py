from discord import Embed, Color

from config import starch

async def starit_mythic(bot, message, name):
  starboard = bot.get_channel(starch)
  staryu = Embed(color=Color.gold())
  staryu.set_footer(text="❤️ The OutN Project")
  staryu.add_field(name='A Mythic Pokémon spawned!',
                   value=f'It\'s **__{name}__** !')
  staryu.add_field(name='Message Link',
                   value=f'[Jump to Message]({message.jump_url})')
  await starboard.send(embed=staryu)
  await message.channel.send(f"Spawn sent to <#{starch}>!")


async def starit_legen(bot, message, name):
  starboard = bot.get_channel(starch)
  staryu = Embed(color=Color.gold())
  staryu.set_footer(text="❤️ The OutN Project")
  staryu.add_field(name='A Legendary Pokémon spawned!',
                   value=f'It\'s **__{name}__** !')
  staryu.add_field(name='Message Link',
                   value=f'[Jump to Message]({message.jump_url})')
  await starboard.send(embed=staryu)
  await message.channel.send(f"Spawn sent to <#{starch}>!")

async def starit_ub(bot, message, name):
  starboard = bot.get_channel(starch)
  staryu = Embed(color=Color.gold())
  staryu.set_footer(text="❤️ The OutN Project")
  staryu.add_field(name='An Ultra Beast Pokémon spawned!',
                   value=f'It\'s **__{name}__** !')
  staryu.add_field(name='Message Link',
                   value=f'[Jump to Message]({message.jump_url})')
  await starboard.send(embed=staryu)
  await message.channel.send(f"Spawn sent to <#{starch}>!")

async def starit_reg(bot, message, name):
  starboard = bot.get_channel(starch)
  staryu = Embed(color=Color.gold())
  staryu.set_footer(text="❤️ The OutN Project")
  staryu.add_field(name='A Regional Pokémon spawned!',
                   value=f'It\'s **__{name}__** !')
  staryu.add_field(name='Message Link',
                   value=f'[Jump to Message]({message.jump_url})')
  await starboard.send(embed=staryu)
  await message.channel.send(f"Spawn sent to <#{starch}>!")
