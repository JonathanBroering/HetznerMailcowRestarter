# HetznerMailcowRestarter
Keeps your Mailcow Server at up and running.
*Using Hetzner (and their API)*

## Background for this Project
I'm using Mailcow for my own mailserver. But sometimes there seems to be a problem causing the Server to stop working. So to keep the Server up at all time, and don't miss any Mails i decided to write this script. It simply checks for 1) a general response from the server (ping request) and 2) if there is any error message from Mailcow itself.
I'm not sure if anyone has the same problem as me, but if so this script might help. 
And of course it has to be run from a diffrent Server, but its very lightweight and can be used on basically any Server.

## What is does
To check if the Mailcow server is up and running it, as mentioned in the Background section, sends a ping request. If the ping is successful it goes on the next stage. It grabs the Website and checks if there is an error message. Due to the use of docker container in Mailcow-dockerized only a part of the software breaks and the web container is still able to tell you that an error has occurred. If there is an error message displayed, or the server isnt repsonding at all it uses the Hetzner API to restart the entire server and brings the Mailcow instance back up

## Download
wget https://raw.githubusercontent.com/jnthn-b/HetznerMailcowRestarter/master/start.py

## Setup
This Script is running using Python3.
You need these Dependencies:
- time
- socket
- requests
- urllib.request

**The Config is in the start.py file itself.**
This are the Configs:

The Hostname of your MailServer (the Mailcow Login Page).
- `host = "mail.example.com"`

The Port to check if the Server is responding (80 - non SSL, 443 - SSL).
- `port = 443 # default: 443`

The Error Message to look out for on the Mailcow Site. This is the default Error message.
- `error = "<br />The following error was reported:<br/>" # error message used by mailcow`

The Delay to check if the Server is online.
- `delay = 60 # in seconds, default: 60`

The Hetzner API token, which can be found here: Open the Project -> Using the Sidebar Navigate to the Access Tab. On the top open the API-Token Menu and generate one.
- `api_token = "********************************************"`

The Server ID of the Mailserver, can be found in the URL if the Server is open (make sure to DO NOT copy the Project ID, but the Server ID)
- `server_id = "********"`

## Start
To run the Script just run it using python:

`python3 start.py`

If you want to run this script in the background use screen:

*This way is recommended to keep the script running in the background*

`screen -AmdS HetznerMailcowRestarter python3 start.py`
