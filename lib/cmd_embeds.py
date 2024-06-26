from discord import Embed, Color


async def help_embed(chnl):
    embed = Embed(
        title="The OutN Project v8",
        url='https://github.com/Pranjal-SB/OutN/',
        color=0x6CB5E5,
        description='An Amazing FOSS Pokémon assist and more bot for the discord game "Poketwo".\nBelow are its features.',
    )
    embed.add_field(
        name="Automatic naming",
        value="OutN automatically recognises the Pokémon and provides its name in the chat as an embed.",
        inline=False,
    )
    embed.add_field(
        name="Rare Ping",
        value="OutN automatically pings the configured role if any mythic, legendary or ultra-beast Pokémon spawns.",
        inline=False,
    )
    embed.add_field(
        name="Regional Ping",
        value="OutN automatically pings the configured role if any Regional Pokémon spawns.",
        inline=False,
    )
    embed.add_field(
        name="Automatic starboard",
        value="OutN automatically sends any rare Pokémon that spawns in the respective starboard channel.",
        inline=False,
    )
    embed.add_field(
        name="Catch logs",
        value="OutN automatically recognises catches and logs them in the respective channel",
        inline=False,
    )
    embed.add_field(
        name="Spawn logs",
        value="OutN automatically records all the spawns in the respective channel",
        inline=False,
    )
    embed.add_field(
        name="Hint solving",
        value="OutN automatically recognises hints and solves them for you.",
        inline=False,
    )
    embed.add_field(
        name="Manual Identification | identify command",
        value="OutN can also manually identify any pokemon and tell you the name.\nJust do 'on.identify' and attach the image to the message",
        inline=False,
    )
    embed.add_field(
        name="Help command",
        value="This message.",
        inline=False,
    )
    embed.set_footer(text="❤️ The OutN Project")
    await chnl.send(embed=embed)

async def identify_embed(message, name):
  embed = Embed(color=Color.blue())
  embed.set_footer(text="❤️ The OutN Project")
  embed.add_field(name='Pokémon Identified!',
                  value=f"It's **__{name}__**! catch it using:")
  embed.add_field(name='Command', value=f"@Pokétwo#8236 c {name}")
  await message.channel.send(embed=embed)
