# dora-the-discordbot

Exploring the discord API and making an unique bot for a server

Everything runs on a Raspberry Pi Zero

secrets.py reads two textfiles:

* token.txt - a file containing only the token for discord

* affirmations.txt - a list of affirmations because why not :) 

## dora_launcher.sh
```
#!/bin/sh
# launcher.sh

sleep 60

cd /
cd home/pi/dora-the-discordbot/

sudo python3 main.py
cd /
```

## dora.service
```
[Unit]
Description=Dora The Discord Bot
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/dora-the-discordbot
ExecStart=/home/pi/dora_launcher.sh

[Install]
WantedBy=multi-user.target
```

Enabling the service


```
sudo systemctl enable dora.service
sudo systemctl start dora.service
``` 



Some quirks:

![Display turning off backlight](https://user-images.githubusercontent.com/38492478/119057459-d3094880-b9cc-11eb-9500-26825bfa2e22.gif)

![Display without backlight](https://user-images.githubusercontent.com/38492478/119057857-8bcf8780-b9cd-11eb-99dc-519136e28a4e.gif)