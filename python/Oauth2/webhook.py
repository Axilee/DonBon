from flask import Flask, request
from urllib.parse import urlencode
import requests
import generateOauth #TYMCZASOWE - zeby sie odpalało przy właczeniu 'python webhook.py'
app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_webhook():
    #zbiera wyslane requesty do nas tutaj 
    code = request.args.get('code') #pobiera ten jebany kod
    scope = request.args.getlist('scope') #pobiera scope permisji //lista
    json = send(code) #json z tokenem, z odpowiedzi po wyslaniu kodu
    access_token = json.get('access_token')
    return f"<H1 style='font-size:5em'>TOKEN ODEBRANY WOOHOO<br><br>TOKEN: {access_token}<br> WYGASA ZA: {round(json.get('expires_in')/60,1)}min<br>REFRESH TOKEN: {json.get('refresh_token')}"

def send(code):
    print(f"generuje linka kodem {code}")
    dane = {
    'client_id' : "nohxc0resfams2ui1ftvvs07awax2c",
    'client_secret' : "k4vzdraf652r8sn6etby4g2ehoji7m",
    'code' : code,
    'grant_type' : "authorization_code",
    'redirect_uri' : "http://localhost:5000"
    }
    uri ='https://id.twitch.tv/oauth2/token?'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    #wyślij POST z kodem, zwraca access token
    odp = requests.post(uri, data = dane, headers = headers) 
    json = odp.json()
    print("WYSŁANO POST\n")
    print(f"KOD ODPOWIEDZI: {odp.status_code}")
    print(f"ACCESS_TOKEN = {json.get('access_token')}")
    print(f"REFRESH_TOKEN = {json.get('refresh_token')}")
    print(f"WYGASA ZA = {round(json.get('expires_in')/60,2)}min")
    

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