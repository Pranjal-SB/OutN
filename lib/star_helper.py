from discord import Embed, Color

from config import starch

async def starit_mythic(bot, message, name):
  starboard = bot.get_channel(starch)
  og_embed = message.embeds[0]
  staryu = Embed(color=Color.gold())
  staryu.set_author(name="Pokétwo", icon_url='https://cdn.discordapp.com/avatars/716390085896962058/3031fa9e2fabde1652a57ab33f4d7f37.webp?size=160')
  staryu.add_field(name=og_embed.title, value=og_embed.description, inline=False)
  staryu.add_field(name='',
                   value=f'[Jump to Message]({message.jump_url})', inline=False)
  staryu.add_field(name='It is a Mythic Pokémon!',
                   value=f'It is **__{name}__** !', inline=False)
  staryu.set_image(url=og_embed.image.url)
  staryu.set_footer(text="❤️ The OutN Project")

  await starboard.send(embed=staryu)
  await message.channel.send(f"Spawn sent to <#{starch}>!")


async def starit_legen(bot, message, name):
  starboard = bot.get_channel(starch)
  og_embed = message.embeds[0]
  staryu = Embed(color=Color.gold())
  staryu.set_author(name="Pokétwo", icon_url='https://cdn.discordapp.com/avatars/716390085896962058/3031fa9e2fabde1652a57ab33f4d7f37.webp?size=160')
  staryu.add_field(name=og_embed.title, value=og_embed.description, inline=False)
  staryu.add_field(name='',
                   value=f'[Jump to Message]({message.jump_url})', inline=False)
  staryu.add_field(name='It is a Legendary Pokémon!',
                   value=f'It is **__{name}__** !', inline=False)
  staryu.set_image(url=og_embed.image.url)
  staryu.set_footer(text="❤️ The OutN Project")
  await starboard.send(embed=staryu)
  await message.channel.send(f"Spawn sent to <#{starch}>!")

async def starit_ub(bot, message, name):
  starboard = bot.get_channel(starch)
  og_embed = message.embeds[0]
  staryu = Embed(color=Color.gold())
  staryu.set_author(name="Pokétwo", icon_url='https://cdn.discordapp.com/avatars/716390085896962058/3031fa9e2fabde1652a57ab33f4d7f37.webp?size=160')
  staryu.add_field(name=og_embed.title, value=og_embed.description, inline=False)
  staryu.add_field(name='',
                   value=f'[Jump to Message]({message.jump_url})', inline=False)
  staryu.add_field(name='It is an Ultra Beast Pokémon!',
                   value=f'It is **__{name}__** !', inline=False)
  staryu.set_image(url=og_embed.image.url)
  staryu.set_footer(text="❤️ The OutN Project")
  await starboard.send(embed=staryu)
  await message.channel.send(f"Spawn sent to <#{starch}>!")

async def starit_reg(bot, message, name):
  starboard = bot.get_channel(starch)
  og_embed = message.embeds[0]
  staryu = Embed(color=0xcfe4e8)
  staryu.set_author(name="Pokétwo", icon_url='https://cdn.discordapp.com/avatars/716390085896962058/3031fa9e2fabde1652a57ab33f4d7f37.webp?size=160')
  staryu.add_field(name=og_embed.title, value=og_embed.description, inline=False)
  staryu.add_field(name='',
                   value=f'[Jump to Message]({message.jump_url})', inline=False)
  staryu.add_field(name='It is a Regional Pokémon!',
                   value=f'It is **__{name}__** !', inline=False)
  staryu.set_image(url=og_embed.image.url)
  staryu.set_footer(text="❤️ The OutN Project")
  await starboard.send(embed=staryu)
  await message.channel.send(f"Spawn sent to <#{starch}>!")
