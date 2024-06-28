
# The OutN Project
> current release : [v8](https://github.com/Pranjal-SB/OutN/blob/main/CHANGELOG.md) [stable](https://github.com/Pranjal-SB/OutN/releases/latest)

An actively developed **Self-hostable FOSS** pokemon recognition and assistant bot for discord and made more specifically for the discord pokemon game "Poketwo".

It can identify Pokémon from Pokétwo spawns, ping a role for rare and regional spawns and pin them, other many features!and it is fully automated and updated.

Made with ❤️ in Python

> Skip to [Usage/installation](https://github.com/Pranjal-SB/OutN/#usage-installation)

## Table of Contents
- [The OutN Project](#the-outn-project)
  - [Features](#features)
  - [Roadmap](#roadmap)
  - [Usage/installation](#usage-installation)
    - [automatic](#automatic)
    - [manual](#manual)
  - [Changelog](#changelog)
  - [FAQ](#faq)
  - [Feedback and Support](#feedback-and-support)
  - [Contributing](#contributing)
  - [Code Of Conduct](#code-of-conduct)
  - [License](#license)
    - [In this case](#in-this-case)
  - [Star History](#star-history)
  - [Authors](#authors)


## Features
- ⭐ can be used to make CUSTOM bots for your server
- ⭐ completely FOSS i.e. Free and Open Source
- ⭐ 'Ai' recognition
- ⭐  built-in Starboard
- Rare and regional ping
- catch logging
- built-in hint solver
- both automatic & manual identification support
- spawn logging
- Pretty embeds
- Self-hostable
- fully customizable
- config based - no coding skills required
- easy to use/Beginner-Friendly
- ezy catch - just copy and paste
- Automatic
- Light and not system heavy
- Cross platform


## Roadmap

- [x] Ai identification <- [v1.0](https://github.com/Pranjal-SB/OutN/blob/main/CHANGELOG.md#v10)
- [x] Rare ping <- [v2.0](https://github.com/Pranjal-SB/OutN/blob/main/CHANGELOG.md#v20)
  - [x] mythic
  - [x] legendary
  - [x] ultra beast
  - [x] regional 
- [x] Embeds <- [v3.0](https://github.com/Pranjal-SB/OutN/blob/main/CHANGELOG.md#v30)
- [x] Hint solver <- [v4.0](https://github.com/Pranjal-SB/OutN/blob/main/CHANGELOG.md#v40)
- [x] StarBoard <- [v5.0](https://github.com/Pranjal-SB/OutN/blob/main/CHANGELOG.md#v50)
- [x] catch logs <- [v6.0](https://github.com/Pranjal-SB/OutN/blob/main/CHANGELOG.md#v60)
- [x] spawn logs <- [v7.0](https://github.com/Pranjal-SB/OutN/blob/main/CHANGELOG.md#v70)
- [x] commands <- [v8.0](https://github.com/Pranjal-SB/OutN/blob/main/CHANGELOG.md#v80)
  - [x] help command
  - [x] identify command
- [ ] more..




## Usage/installation

download the OutN bot by 
- [latest stable release](https://github.com/Pranjal-SB/OutN/releases/latest)
- [source code](https://github.com/Pranjal-SB/OutN/archive/refs/heads/main.zip)

1. make a discord bot - [guide](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token#creating-a-bot) / [official page](https://discord.com/developers/applications/)
2. star [this repo](https://github.com/Pranjal-SB/OutN) 😉 ~~plz~~
3. follow any of the below methods for usage


### automatic

extract the folder just run 'run.bat'

it will install dependencies and run the program by itself

for further usage i.e. not the first run and the dependencies are all already installed

you can just run 'just_run.bat' which will only run main.py and nothing else

### manual

- requires 
  - [python](https://www.python.org/) to be installed

extract the folder and open a command prompt window in it

1. install dependencies using:
  ```
  pip install aiohttp discord numpy pillow tensorflow configparser
  ```
2. then run the program using:
  ```
  python main.py
  ```
>  the program will ask for your [bot token](https://www.writebots.com/discord-bot-token/), [role ids](https://discordhelp.net/role-id) (for rare and regional ping) and [channel id](https://turbofuture.com/internet/Discord-Channel-ID) (for starboard, catch and spawn logger) on initialisation and then will save it to 'config.ini' so that it does not ask you every time it runs.

> [!NOTE]
> the token is only saved locally and is not sent anywhere.

> [!CAUTION]
> make sure not to upload 'config.ini' anywhere as it contains your bot token.



## Changelog

[CHANGELOG.md](https://github.com/Pranjal-SB/OutN/blob/main/CHANGELOG.md)


## FAQ

Q) I got this error ``` ModuleNotFoundError: No module named '<module name>' ``` what do i do?

A) do ```pip install <modulename>```

rest -> you tell me 😆


## Feedback and Support

All and every kind of feedback is welocome.
And any constructive criticism is appreciated.

If you have any kind of feedback or need help feel free to contact me:
- Discord 
  - [@mr.linear](https://discordapp.com/users/1140568955220656160)
  - [OutN support \[in development\]](https://discord.gg/aMJzFJsf)


## Contributing

Contributions are always welcome!

currently you can:
- contribute by fixing any bugs in the code you find
- suggesting features


## Code Of Conduct

Please Adhere to the [Code of Conduct](https://github.com/Pranjal-SB/OutN?tab=coc-ov-file)

## License

[No License](https://choosealicense.com/no-permission/)
#### In this case
- you are **free to use** and share the software as long as you `give credit` to the developer a.k.a myself which is only fair.
- you have no permission from the creator of the software to modify, or share the software `without credits` or `without permission`. Although a code host such as GitHub may allow you to view and fork the code, this does not imply that you are permitted to modify, or share the software for any purpose or without permission.

## Star History

<a href="https://star-history.com/#Pranjal-SB/OutN&Date"><picture><source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Pranjal-SB/OutN&type=Date&theme=dark" /><source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Pranjal-SB/OutN&type=Date" /><img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Pranjal-SB/OutN&type=Date" /></picture></a>



## Authors

- [Myself](https://github.com/Pranjal-SB)
