import time
import socket
import requests
import urllib.request

# C O N F I G
host = "mail.example.com"
port = 443 # default: 443
error = "<br />The following error was reported:<br/>" # error message used by mailcow
delay = 60 # in seconds, default: 60
api_token = "**************************************"
server_id = "*******"
# C O N F I G

def response_check():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    if result == 0:
        print("[Okay] [1/2]Server is responding")
        error_check()
    else:
        print("[ERROR][1/2]Server is NOT responding")
        restart()

def error_check():
    response = urllib.request.urlopen("https://" + host)
    page_source = response.read().decode('utf-8')
    if error in page_source:
        print("[ERROR][2/2]Error detected!")
        restart()
    else:
        print("[Okay] [2/2]No Error detected!")

def restart():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_token,
    }
    response = requests.post('https://api.hetzner.cloud/v1/servers/' + server_id +'/actions/reboot', headers=headers)
    time.sleep(120)


while True:
    response_check()
    time.sleep(delay)
