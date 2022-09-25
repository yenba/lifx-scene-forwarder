import os
import configparser
from fastapi import FastAPI
import requests
import pandas as pd

# setup variables
CONFIGFILENAME = 'config/lifxconfig.cfg'
TOKEN_LENGTH = 64
DEFAULT_LIFX_API_KEY = ''
LIFX_API_KEY = DEFAULT_LIFX_API_KEY

# setup function to read config file


def process_config(config_filename):

    global LIFX_API_KEY
    LIFX_API_KEY = DEFAULT_LIFX_API_KEY
    CONFIG_FILE_PATH = os.getcwd() + os.path.sep + config_filename

    parser = configparser.ConfigParser()
    if parser.read(CONFIG_FILE_PATH):

        try:
            config_token = parser.get('config', 'LIFX_API_KEY')
            if len(config_token) == TOKEN_LENGTH:
                LIFX_API_KEY = 'Bearer ' + config_token
            else:
                print(
                    '\033[31mInvalid LIFX API Key from config file; assumed None\033[0m')
                LIFX_API_KEY = DEFAULT_LIFX_API_KEY
        except:
            pass


# process the config file
process_config(CONFIGFILENAME)

# Get all scenes to use later


def GetScenes():
    url = "https://api.lifx.com/v1/scenes"
    headers = {
        'Authorization': LIFX_API_KEY
    }
    sceneList = requests.request("GET", url, headers=headers, timeout=30)
    j = sceneList.json()
    df = pd.json_normalize(j)
    return df


# create the API
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/scenes/{sceneName}")
async def read_item(sceneName):
    # for each row in the scenes dataframe
    for index, row in GetScenes().iterrows():
        # if the row name (removing spaces) equals the input scene name then do the stuff below
        if row['name'].replace(" ", "") == sceneName:
            urlPart1 = "https://api.lifx.com/v1/scenes/scene_id:"
            urlPart2 = row['uuid']
            urlPart3 = "/activate"
            fullUrl = urlPart1 + urlPart2 + urlPart3
            headers = {
                'Authorization': LIFX_API_KEY
            }
            # run the put command
            response = requests.request(
                "PUT", fullUrl, headers=headers, timeout=30)
            return response.json()
