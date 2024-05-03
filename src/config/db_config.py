import json

def load_conf() -> dict:
    with open('src/config/config.json','r') as f:
        return json.load(f)['mysql']    