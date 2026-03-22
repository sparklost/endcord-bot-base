# endcord-bot-base
An extension for [endcord](https://github.com/sparklost/endcord) discord TUI client, that implements minimal bot with interactions.  
This extension is intended **for bots only**.  

## Installing
See [official extensions documentation](https://github.com/sparklost/endcord/blob/main/extensions.md#installing-extensions) for installing instructions.
Available options:
- Git clone into `Extensions` directory located in endcord config directory.
- Run `endcord -i https://github.com/sparklost/endcord-bot-base`
- Or use endcord client-side command `install_extension sparklost/endcord-bot-base`


## Configuration
Edit `commands.json` to add commands, but it wont do anything on its own.  
See [extnsion documentation](https://github.com/sparklost/endcord/blob/main/docs/extensions.md#creating-bots) for more info on creating bots and handling commands.  
After updating `commands.json` run bot inside endcord, and run `bot_register_commands`. It will register new and update old commands one-by-one. Check log for any issues.  
Note that there is a limit of 200 command registrations per day.  

## Disclaimer
This extension is usable only in bots which should not be breaking any ToS, byt here's a warning anyway:  
> [!WARNING]
> Using third-party client is against Discord's Terms of Service and may cause your account to be banned!  
> **Use endcord and/or this extension at your own risk!**  
> If this extension is modified, it may be used for harmful or unintended purposes.  
> **The developer is not responsible for any misuse or for actions taken by users.**  
