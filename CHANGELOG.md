## v1.0
- First stable release
- 'Ai' identification
- ezy catch
- added easy setup -> config

## v2.0
- added rare ping
- fixed bugs

## v3.0
- switched to embeds
- optimised code

## v3.1
- upgraded embeds -> separated mythic, legendary and ub 
- optimised rare ping
- optimised code

## v4.0
- added hint solver
- upgraded embeds
- upgraded rare ping
    - added regional support
- multifile system for easier code reading and editing

## v5.0
- added STARBOARD!!
    - added starboard to config
- fixed bugs
    - hint not working

## v6.0
- added catch log
- upgraded config system
    - made rare ping optional
    - made regional ping optional
    - made starboard optional
    - made catch log optional
    - i.e made everything optional

## v6.1
- cleaned up program directory
    - made folder 'lib'
- fixed catch logger

## v7.0
- cleaned up program directory even more i.e. made it even better
- added spawn logger
    - optional ofc.
- fixed a couple minor bugs

## v7.1
- optimized code
- removed useless files and parts

## v8
- added commands!!!
    - added help command
    - added identify command

## v9
- upgraded starboard
- fixed tier detection
    - rare pokémon were matched as substrings of a text blob, so 'eternatus' counted as legendary because it contains 'natu'
    - galarian articuno, ting-lu and both zygarde forms were misnamed in the data files and never got a rare ping
    - tier lists are now exact-match sets checked against the model's own class names
- fixed the bot freezing on every spawn
    - image recognition now runs off the event loop instead of blocking the whole bot
- fixed crashes
    - failed image downloads and unreadable images no longer kill the handler
    - images with transparency are converted properly before recognition
    - a wrong or missing channel ID is now ignored instead of throwing
- fixed config
    - leaving a y/n question blank used to switch the feature ON and ping a broken role
- fixed hint solving
    - hints are no longer compiled as regex, so nobody can hang the bot with a crafted message
- commands now have to start with 'on.' instead of merely containing it
- added a self-check (`python test_outn.py`) covering tier lookup and hint solving
- optimised code
    - one shared HTTP session instead of a new one per spawn
    - merged the four starboard functions and the five spawn embeds
    - trimmed requirements.txt from 46 pinned packages to the 5 actually used
    - added .gitignore so config.ini (your bot token) can't be committed