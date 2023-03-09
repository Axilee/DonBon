import generateOauthUnified
import webhookUnified
from webhookUnified import flaskAppWebhook
import urllib.parse
def test():
    service_name = "spotify"
    client_id = "4ea71c707b2b4345b495f5edbba034a0"
    client_secret = "f46ac03a5b654dda94dc124003d6a6b5"
    uri = 'https://accounts.spotify.com/'
    redirect_uri = 'http://localhost:5000/callback'
    if(service_name == "spotify"):
        redirect_parsed_uri = urllib.parse.quote(redirect_uri, safe="")
        oAuth = generateOauthUnified.getOAuth(service_name,client_id,uri,redirect_parsed_uri)

    app = flaskAppWebhook(service_name,client_id,client_secret,redirect_uri)

    if __name__ == '__main__':
        app.run(host="0.0.0.0", port=5000)