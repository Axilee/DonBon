from flask import Flask, request
from urllib.parse import urlencode
import requests
#import AuthorizationOauth2 #TYMCZASOWE - zeby sie odpalało przy właczeniu 'python webhook.py'
import base64
import time
import asyncio

start_time = time.time()

app = Flask(__name__)
async def flaskAppWebhook(service_name,client_id,client_secret,redirect_uri):

    client_encoded = client_id + ":" + client_secret
    sample_string_bytes = client_encoded.encode("ascii")
    
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    @app.route('/', methods=['GET'])
    def handle_webhook():

            #zbiera wyslane requesty do nas tutaj 
            code = request.args.get('code') #pobiera ten jebany kod
            scope = request.args.getlist('scope') #pobiera scope permisji //lista
            json = send(code) #json z tokenem, z odpowiedzi po wyslaniu kodu
            access_token = json.get('access_token')
            print(access_token)
            return f"<H1 style='font-size:5em'>TOKEN ODEBRANY WOOHOO<br><br>TOKEN: {access_token}<br> WYGASA ZA: {round(json.get('expires_in')/60,1)}min<br>REFRESH TOKEN: {json.get('refresh_token')}"
            return access_token
    @app.route('/callback', methods=['GET'])
    def handle_callback():

            #zbiera wyslane requesty do nas tutaj 
            code = request.args.get('code') #pobiera ten jebany kod
            scope = request.args.getlist('scope') #pobiera scope permisji //lista
            json = send(code) #json z tokenem, z odpowiedzi po wyslaniu kodu
            access_token = json.get('access_token')
            print(access_token)
            return f"<H1 style='font-size:5em'>TOKEN ODEBRANY WOOHOO<br>Do serwisu: {service_name}<br>TOKEN: {access_token}<br><br>REFRESH TOKEN: {json.get('refresh_token')}"

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
                "Authorization": "Basic " + base64_string
                }
        #wyślij POST z kodem, zwraca access token
        odp = requests.post(uri,headers = headers , data = dane)
        json = odp.json()
        print("WYSŁANO POST\n")
        print(f"Auth code: {code}")
        print(f"Client encode {base64_string}")
        print(f"KOD ODPOWIEDZI: {odp.status_code}")
        print(f"ACCESS_TOKEN = {json.get('access_token')}")
        print(f"REFRESH_TOKEN = {json.get('refresh_token')}")
        #print(f"WYGASA ZA = {round(json.get('expires_in')/60,2)}min")
        
        #while True:
        #    current_time = time.time()
        #    elapsed_time = current_time - start_time
        #    if elapsed_time >= 120:
        #        print("Minął czas")
        #        break
        #    time.sleep(1)

        return json #wysyla json do handle_webhook
    return app

