

import multiprocessing
import webhook
import AuthorizationOauth2  
import urllib.parse
import configparser
import tkinter as tk
import os
from PIL import ImageTk, Image #pip install pillow
from wsgiref.simple_server import make_server

#global config load

class inicjalizuj():

    def hook():
        httpd = make_server('localhost',5000,webhook.flaskAppWebhook.app)
        httpd.serve_forever()
    wh = multiprocessing.Process(target=hook)
    def wybor(self):
        
        config = configparser.ConfigParser()
        config.read("identity.ini")
        print (config['TWITCH'])
        def btn_tw():
            c = config['TWITCH']
            redirect_parsed_uri = urllib.parse.quote(c['redirect_uri'], safe="")
            oAuth = AuthorizationOauth2.getOAuth(c['service_name'],c['client_id'],c['uri'],redirect_parsed_uri)
        def btn_sp():
            c = config['SPOTIFY']
            redirect_parsed_uri = urllib.parse.quote(c['redirect_uri'], safe="")
            oAuth = AuthorizationOauth2.getOAuth(c['service_name'],c['client_id'],c['uri'],redirect_parsed_uri)


        
        #------ okno wyboru/konfiguracja okna
        okno = tk.Tk()
        okno.geometry('804x410')
        okno.title('Autoryzacja')
        okno.configure(bg="#1c1b22")
        imgtw = Image.open("ikonki/twitch.png")
        imgsp = Image.open("ikonki/spotify.png")
        resizedtw = imgtw.resize((400,400),Image.LANCZOS)
        resizedsp = imgsp.resize((400,400),Image.LANCZOS)
        twico = ImageTk.PhotoImage(resizedtw)
        spico = ImageTk.PhotoImage(resizedsp)
        btntw = tk.Button(okno,bd=0, command=btn_tw,image=twico, bg="#1c1b22")
        btnsp = tk.Button(okno,bd=0, command=btn_sp,image=spico, bg="#1c1b22")
        btntw.grid(row=0,column=0)
        btnsp.grid(row=0,column=1)
        okno.mainloop() #start okno dopoki sie nie zamknie
        # wh.join() #zakoncz proces webhooka
        #app = webhook.flaskAppWebhook(service_name,client_id,client_secret,redirect_uri)
    
if __name__ == "__main__":
    inicjalizuj().wh.start()
    inicjalizuj().wybor()
    inicjalizuj().wh.terminate()