import requests

# Base address for my Nanoleaf
base_address = "http://192.168.68.129:16021/api/v1/hQfmNSrfeYyNn8i0JoD91qRvpX5DJ3hW/state"
# API key

def change_color(n):
    r = requests.put(base_address, json={ "hue": { "value": int(color) }})
    return r.content

