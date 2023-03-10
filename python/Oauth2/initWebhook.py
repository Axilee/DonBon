import AuthorizationOauth2
import webhook
import urllib.parse
import configparser
import tkinter as tk
import multiprocessing
#global config load
config = configparser.ConfigParser()
dane = config.read("identity.ini")
print(dane)

class inicjalizuj():
    
    
    # service_name = "spotify"
    # client_id = "4ea71c707b2b4345b495f5edbba034a0"
    # client_secret = "f46ac03a5b654dda94dc124003d6a6b5"
    # uri = 'https://accounts.spotify.com/'
    # redirect_uri = 'http://localhost:5000/callback'
    def wybor():
        def btn_tw():
            c = config['TWITCH']
            print("twitch przycisk")
            redirect_parsed_uri = urllib.parse.quote(c['redirect_uri'], safe="")
            oAuth = AuthorizationOauth2.getOAuth("twitch",c['client_id'],c['uri'],redirect_parsed_uri)
        def btn_sp():
            c = config['SPOTIFY']
            print("spotify przycisk")
            redirect_parsed_uri = urllib.parse.quote(c['redirect_uri'], safe="")
            oAuth = AuthorizationOauth2.getOAuth('spotify',c['client_id'],c['uri'],redirect_parsed_uri)
        okno = tk.Tk()
        okno.geometry('1280x300')
        okno.title('Autoryzacja')
        btntw = tk.Button(okno, text="Twitch", command=btn_tw, font="'Arial', 72")
        btnsp = tk.Button(okno, text="Spotify", command=btn_sp, font="'Arial', 72")
        btntw.place(x=10,y=50, width=640, height=200)
        btnsp.place(x=660,y=50,width=640, height=200)
        okno.mainloop()
    # app = webhook.flaskAppWebhook(service_name,client_id,client_secret,redirect_uri)
    # if __name__ == '__main__':
    #     app.run(host="0.0.0.0", port=5000)

inicjalizuj.wybor()