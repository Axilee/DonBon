#tworzy okno wyboru autoryzacji spotify/twitch, pobiera z identity.ini parametry do autoryzacji, wlacza webhook i tworzy tokeny // TODO zwracanie tokenow gdzies


from Oauth2 import webhook
from Oauth2 import AuthorizationOauth2  #<- najwyrazniej trzeba tak importowac zeby sie dalo potem z gory importowac, pojebane
import urllib.parse
import configparser
import tkinter as tk
import _tkinter
import os
from PIL import ImageTk, Image #pip install pillow
#global config load
config = configparser.ConfigParser()
dane = config.read("identity.ini")
print(dane)

class inicjalizuj():
    def wybor():
        print ("WYBOR")
        def btn_tw():
            c = config['TWITCH']
            print("twitch przycisk")
            redirect_parsed_uri = urllib.parse.quote(c['redirect_uri'], safe="")
            oAuth = AuthorizationOauth2.getOAuth(c['service_name'],c['client_id'],c['uri'],redirect_parsed_uri)
            app = webhook.flaskAppWebhook(c['service_name'],c['client_id'],c['client_secret'],c['redirect_uri'])
            app.run()
        def btn_sp():
            c = config['SPOTIFY']
            print("spotify przycisk")
            redirect_parsed_uri = urllib.parse.quote(c['redirect_uri'], safe="")
            oAuth = AuthorizationOauth2.getOAuth(c['service_name'],c['client_id'],c['uri'],redirect_parsed_uri)
            app = webhook.flaskAppWebhook(c['service_name'],c['client_id'],c['client_secret'],c['redirect_uri'])
            app.run()


             
        # if __name__ == "__main__":
        #     app.run(host="0.0.0.0", port=5000)
        #     wh = multiprocessing.Process(target=zlapWebhook)
        #     wh.start()  #rozpocznij proces webhook w tle
        

        #------ okno wyboru/konfiguracja okna
        okno = tk.Tk()
        okno.geometry('804x410')
        okno.title('Autoryzacja')
        okno.configure(bg="#1c1b22")
        imgtw = Image.open("Oauth2/ikonki/twitch.png")
        imgsp = Image.open("Oauth2/ikonki/spotify.png")
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
    
