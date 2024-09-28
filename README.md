# Giveaway Bot
- basic script of discord giveaways bot written on Python
- all thanks goes to [Dummylot](https://github.com/dummylot) for help in this project
# How to run this project
- you can run this project by 2 ways
## 1 - From Termux
- you should download [main.py](https://github.com/MohamedLunar/giveaway-bot/blob/main/main.py) and [requirements.txt](https://github.com/MohamedLunar/giveaway-bot/blob/main/requirements.txt)
- updating data for install
``` bash
apt update && apt upgrade
```
- allow access for run the file
``` bash
termux-setup-storage
cd /sdcard/download
```
- install pakages
``` bash
pkg install python
```
- install the requirements from [requirements.txt](https://github.com/MohamedLunar/giveaway-bot/blob/main/requirements.txt)
``` bash
pip install -r requirements.txt
```
- run the file
``` bash
python main.py
```
- remember to edit your token and your status in [main.py](https://github.com/MohamedLunar/giveaway-bot/blob/main/main.py) file
## 2 - From a host
- the best free host is [PylexNodes](https://pylexnodes.net) you should host from it
- create new server then upload [main.py](https://github.com/MohamedLunar/giveaway-bot/blob/main/main.py) file
- then go to startup and scroll down to **Additional Python packages** and type **discord** to install discord.py library
- remember to edit your token and your status in [main.py](https://github.com/MohamedLunar/giveaway-bot/blob/main/main.py) file
- after do all of those go to **console** and select **start** then the bot will say `logged in as {your.bot.name} successfully`
# Command usage
- to run the giveaway you should do
`g!start <duration in seconds> <prize>`
- other command
`g!help`
