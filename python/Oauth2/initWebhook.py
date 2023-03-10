import AuthorizationOauth2
import webhook
import urllib.parse
import configparser
import tkinter as tk
import multiprocessing
import os
from PIL import ImageTk, Image #pip install pillow
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
        okno.geometry('804x410')
        okno.title('Autoryzacja')
        okno.configure(bg="#1c1b22")
        imgtw = Image.open("./ikonki/twitch.png")
        imgsp = Image.open("./ikonki/spotify.png")
        resizedtw = imgtw.resize((400,400),Image.LANCZOS)
        resizedsp = imgsp.resize((400,400),Image.LANCZOS)
        twico = ImageTk.PhotoImage(resizedtw)
        spico = ImageTk.PhotoImage(resizedsp)
        btntw = tk.Button(okno,bd=0, command=btn_tw,image=twico, bg="#1c1b22")
        btnsp = tk.Button(okno,bd=0, command=btn_sp,image=spico, bg="#1c1b22")
        btntw.grid(row=0,column=0)
        btnsp.grid(row=0,column=1)
        okno.mainloop()
    # app = webhook.flaskAppWebhook(service_name,client_id,client_secret,redirect_uri)
    # if __name__ == '__main__':
    #     app.run(host="0.0.0.0", port=5000)

inicjalizuj.wybor()