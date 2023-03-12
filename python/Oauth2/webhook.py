from flask import Flask, request
from urllib.parse import urlencode
import requests
#import AuthorizationOauth2 #TYMCZASOWE - zeby sie odpalało przy właczeniu 'python webhook.py'
import base64
import time
import configparser

start_time = time.time()
config = configparser.ConfigParser()
konfig = config.read("Oauth2/identity.ini")
print(f"{konfig} CONFIG WEBHOOKA")
class flaskAppWebhook():
    app = Flask(__name__)

    # client_encoded = client_id + ":" + client_secret
    # sample_string_bytes = client_encoded.encode("ascii")
    
    # base64_bytes = base64.b64encode(sample_string_bytes)
    # base64_string = base64_bytes.decode("ascii")
    
    def send(code, service_name,client_id,client_secret,redirect_uri):
        if service_name.lower() == "twitch":
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
            base64_string = None #bo spotify takie ma
        elif service_name.lower() == "spotify":
            client_encoded = client_id + ":" + client_secret
            sample_string_bytes = client_encoded.encode("ascii")    
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
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
        return json
    @app.route('/', methods=['GET'])
    # def handle_webhook():

    #         #zbiera wyslane requesty do nas tutaj 
    #         code = request.args.get('code') #pobiera ten jebany kod
    #         scope = request.args.getlist('scope') #pobiera scope permisji //lista
    #         json = send(code) #json z tokenem, z odpowiedzi po wyslaniu kodu
    #         access_token = json.get('access_token')
    #         print(access_token)
    #         return f"<H1 style='font-size:5em'>TOKEN ODEBRANY WOOHOO<br><br>TOKEN: {access_token}<br> WYGASA ZA: {round(json.get('expires_in')/60,1)}min<br>REFRESH TOKEN: {json.get('refresh_token')}"
    #         return access_token
    

    @app.route('/callback', methods=['GET'])
    def handle_callback():
            code = request.args.get('code') #pobiera ten jebany kod
            scope = request.args.getlist('scope') #pobiera scope permisji //lista
            state = request.args.get('state')
            #znajdz czy to request ze spotify czy twitch
            if state:
                service_name = "TWITCH"
                c = config[service_name]
                json = flaskAppWebhook.send(code,c['service_name'],c['client_id'],c['client_secret'],c['redirect_uri'])#json z tokenem, z odpowiedzi po wyslaniu kodu
                access_token = json.get('access_token')
                refresh_token = json.get('refresh_token')
                config.set(service_name,'access_token', access_token)
                config.set(service_name,'refresh_token', refresh_token)
                with open('Oauth2/identity.ini','w') as f:
                     config.write(f)
            else:
                service_name = "SPOTIFY"
                c = config[service_name] #nie jestem z tego dumny, ale działa (mozna sprawdzic czy to twitch czy spotify po zwroconym scope, czy zgadza sie z identity.ini, ale to trzeba przerabiać z urlencoded a mi sie nie chce)
                json = flaskAppWebhook.send(code,c['service_name'],c['client_id'],c['client_secret'],c['redirect_uri'])#json z tokenem, z odpowiedzi po wyslaniu kodu
                access_token = json.get('access_token')
                refresh_token = json.get('refresh_token')
                config.set(service_name,'access_token', access_token)
                config.set(service_name,'refresh_token', refresh_token)
                with open('Oauth2/identity.ini','w') as f:
                    config.write(f)
            return f"<H1 style='font-size:5em'>TOKEN ODEBRANY WOOHOO<br>Do serwisu: {service_name}<br>TOKEN: {access_token}<br><br>REFRESH TOKEN: {refresh_token}"

        #print(f"WYGASA ZA = {round(json.get('expires_in')/60,2)}min")
        
        #while True:
        #    current_time = time.time()
        #    elapsed_time = current_time - start_time
        #    if elapsed_time >= 120:
        #        print("Minął czas")
        #        break
        #    time.sleep(1)

         #wysyla json do handle_webhook
   

