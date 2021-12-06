import configparser
import requests

#read ini file
parser = configparser.ConfigParser()
parser.read('score_api.ini')

v_active_env=parser['activeEnv']['env']
v_token_url=parser[v_active_env]['token_url']
v_ecom_url=parser[v_active_env]['ecom_url']
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
        return(body['sessionKey'])

    except:
        print("Error get token")

#get chrono for a case
def get_chrono(v_sessionKey, v_casRef):
    #build chorno url
    v_url = v_ecom_url + "/chrono"
    #request parameter
    v_params={'casRef':v_casRef}
    #request payload - empty for a get request
    payload = {}
    #request header
    headers = {
        'iMX-Session-Key': v_sessionKey,
        'Content-Type': 'application/json',
        'Accept-Language': 'AN'
    }
    #call to API
    try:
        response = requests.get(v_url, headers=headers, data=payload, params=v_params)
        body=response.json()
        print(body)
    except:
        print("Error get chrono for case {}".format(str(v_casRef)))

def main():
    v_sessionKey = get_token()
    #v_chrono_response = get_chrono(v_sessionKey,'2110140101')
    get_chrono(v_sessionKey,'2110140101')
    #print(v_chrono_response)

if __name__ == "__main__":
    main()