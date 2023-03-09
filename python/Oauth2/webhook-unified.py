from flask import Flask, request
from urllib.parse import urlencode
import requests
import generateOauthUnified #TYMCZASOWE - zeby sie odpalało przy właczeniu 'python webhook.py'
import base64

app = Flask(__name__)

service_name = "spotify"
client_id = "4ea71c707b2b4345b495f5edbba034a0"
client_secret = "f46ac03a5b654dda94dc124003d6a6b5"
redirect_uri = "http%3A%2F%2Flocalhost%3A5000%2Fcallback"

client_encoded = client_id + ":" + client_secret
sample_string_bytes = client_encoded.encode("ascii")
  
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")

generateOauthUnified.getOAuth("spotify","4ea71c707b2b4345b495f5edbba034a0","https://accounts.spotify.com/","http%3A%2F%2Flocalhost%3A5000%2Fcallback")
@app.route('/', methods=['GET'])
def handle_webhook():

        #zbiera wyslane requesty do nas tutaj 
        code = request.args.get('code') #pobiera ten jebany kod
        scope = request.args.getlist('scope') #pobiera scope permisji //lista
        json = send(code) #json z tokenem, z odpowiedzi po wyslaniu kodu
        access_token = json.get('access_token')
        print(access_token)
        return f"<H1 style='font-size:5em'>TOKEN ODEBRANY WOOHOO<br><br>TOKEN: {access_token}<br> WYGASA ZA: {round(json.get('expires_in')/60,1)}min<br>REFRESH TOKEN: {json.get('refresh_token')}"

@app.route('/callback', methods=['GET'])
def handle_callback():

        #zbiera wyslane requesty do nas tutaj 
        code = request.args.get('code') #pobiera ten jebany kod
        scope = request.args.getlist('scope') #pobiera scope permisji //lista
        json = send(code) #json z tokenem, z odpowiedzi po wyslaniu kodu
        access_token = json.get('access_token')
        print(access_token)
        return f"<H1 style='font-size:5em'>TOKEN ODEBRANY WOOHOO<br><br>TOKEN: {access_token}<br><br>REFRESH TOKEN: {json.get('refresh_token')}"

def send(code):
    if service_name == "twitch":
        dane = {
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code,
            'grant_type': "authorization_code",
            'redirect_uri': redirect_uri,
        }
        uri = 'https://id.twitch.tv/oauth2/token?'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    elif service_name == "spotify":
        dane = {
            'code': code,
            'grant_type': "authorization_code",
            'redirect_uri': redirect_uri
            }
        uri = "https://accounts.spotify.com/api/token"
        headers = {
             "Authorization": "Basic " + client_encoded
             }
    #wyślij POST z kodem, zwraca access token
    odp = requests.post(uri,headers = headers , data = dane) 
    json = odp.json()
    print("WYSŁANO POST\n")
    print(f"Auth code: {code}")
    print(f"Client encode {base64_string}")
    print(dane,uri,headers)
    print(f"KOD ODPOWIEDZI: {odp.status_code}")
    print(f"ACCESS_TOKEN = {json.get('access_token')}")
    print(f"REFRESH_TOKEN = {json.get('refresh_token')}")
    #print(f"WYGASA ZA = {round(json.get('expires_in')/60,2)}min")
    

    return json #wysyla json do handle_webhook

#init
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


    
# przyklad parametrow linka do wyslania postem, zeby kodem odebrac auth token 

# client_id=hof5gwx0su6owfnys0yan9c87zr6t
# &client_secret=41vpdji4e9gif29md0ouet6fktd2
# &code=gulfwdmys5lsm6qyz4xiz9q32l10
# &grant_type=authorization_code
# &redirect_uri=http://localhost:3000