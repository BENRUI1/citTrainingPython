import configparser
import requests

#read ini file
parser = configparser.ConfigParser()
parser.read('score_api.ini')

v_active_env=parser['activeEnv']['env']
v_token_url=parser[v_active_env]['token_url']
v_apiKey=parser[v_active_env]['apiKey']

#get token
def get_token():
    v_params = {'apiKey': v_apiKey}
    response = requests.get(v_token_url,
                            params=v_params)
    print(response.url)

    v_url=response.url

    try:
        response = requests.get(v_url)
        body = response.json()
        print(body)

    except:
        print("Error get token")

def main():
    get_token()

if __name__ == "__main__":
    main()