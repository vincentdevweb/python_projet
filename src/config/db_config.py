import json

def load() -> dict:
    with open('src/config/config.json','r') as config_file:
        return json.load(config_file)['mysql']

# test return values of the config.json file
if __name__ == '__main__':
    config = load()
    print(config)
    