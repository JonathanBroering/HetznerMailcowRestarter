# HetznerMailcowRestarter
Restarts your Hetzner Online Mailserver (running Mailcow) if the Mailserver isn't responding.

## Background for this Project
I'm using Mailcow for my mailserver. But sometimes there seems to be a problem causing the Server to not work again. So to keep the Server up at all time, and don't miss any Mails i decided to write this script. It simply checks for 1) a general response from the server and 2) if there is any error message from Mailcow itself.
I'm not sure if anyone has the same problem as me, but if so this script might help. 
And of course it has to be run from a diffrent Server, but its very lightweight and can be used on basically any Server.

## Download
wget https://raw.githubusercontent.com/jnthn-b/HetznerMailcowRestarter/master/start.py

## Setup
This Script is running using Python3.
You need these Dependencies:
- time
- socket
- requests
- urllib.request

The Config is in the start.py file itself. 
This are the Configs:
- host = "mail.example.com"
The Hostname of your MailServer (the Mailcow Login Page).
- port = 443 # default: 443
The Port to check if the Server is responding (80 - non SSL, 443 - SSL). 
- error = "<br />The following error was reported:<br/>" # error message used by mailcow
The Error Message to look out for on the Mailcow Site. This is the default Error message.
- delay = 60 # in seconds, default: 60
The Delay to check if the Server is online.
- api_token = "********************************************+++"
The Hetzner API token, which can be found here: Open the Project -> Using the Sidebar Navigate to the Access Tab. On the top open the API-Token Menu and generate one.
- server_id = "*******"
The Server ID of the Mailserver, can be found in the URL if the Server is open (make sure to DO NOT copy the Project ID, but the Server ID)

## Start
To run the Script just run it using python:
jonathan@s3:~# `python3 start.py`
If you want to run this script in the background use screen:
jonathan@s3:~# `screen -AmdS HetznerMailcowRestarter python3 start.py`
