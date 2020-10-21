import requests

# Base address for my Nanoleaf
base_address = "http://192.168.68.129:16021/api/v1/"
# API key
api_key = "hQfmNSrfeYyNn8i0JoD91qRvpX5DJ3hW"

def change_color(color):
    print(color)
    r = requests.put(base_address + api_key + "/state", json={ "hue": { "value": int(color) }, "sat": { "value": 100 }})
    return r.content

def off():
    requests.put(base_address + api_key + "/state", json={ "on": { "value": False }})

def white():
    requests.put(base_address + api_key + "/state" + '/sat', json={ "sat": { "value": 0 }})
