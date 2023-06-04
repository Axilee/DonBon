import os
import time
import asyncio
from twitchio.ext import pubsub
from datetime import datetime
from twitchio.ext import commands
import twitchio
import win32com.client as comclt
import win32api
import win32con
import configparser
import ssh
from SpotifyGrapper import getCurrentlyPlaying
import urllib.parse
from wsgiref.simple_server import make_server
#from Chat import chat
import sys
import multiprocessing
import requests
sys.path.append('Oauth2')
from Oauth2 import webhook
from Oauth2 import AuthorizationOauth2 
from Oauth2 import initWebhook
from pointbits import pointbits
import pointbits as pb
import komendy
import argparse

webhook = webhook.flaskAppWebhook()

#wczytaj konfig zmienne.ini
config = configparser.ConfigParser()
config.read("zmienne.ini")
identity = configparser.ConfigParser()
identity.read("Oauth2/identity.ini")
parser = argparse.ArgumentParser()
parser.add_argument("-p","--purge",action="store_true")
ar = parser.parse_args()
if ar.purge:
    pb.purge()
    exit()


user_token = identity['TWITCH']['access_token'] #zaczyt tokenu auth dla twitch
refresh_token = identity['TWITCH']['refresh_token'] #imo lepiej tutac execowac refresh token bedzie latwiej go responsem odnawiac 
client_id = identity["TWITCH"]['client_id']
client_secret = identity["TWITCH"]['client_secret']
spotify_user_token = identity['SPOTIFY']['access_token']
spotify_refresh_token = identity['SPOTIFY']['refresh_token']
#ewentualnie odczyt/zapis konfiguracji co godzine a generowanie tokenu gdzie indziej



#dane połączenia

ACCESS_TOKEN = '160g7wv175m4mjwzfpd071k5ww8pvx'

PREFIX = "$"

INITIAL_CHANNELS=["DonHoman"]




#--------------------------------------GLOBALNE FUNKCJE ---------------------------------
#sprawdz status komendy z zmienne ini
def sprawdz(typ,nazwa):
    config.get(typ, nazwa)

def wlacz_webhook():
            httpd = make_server('localhost',5000,initWebhook.webhook.flaskAppWebhook.app)
            httpd.serve_forever()
def okno():
        initWebhook.inicjalizuj.wybor()
        identity.read("Oauth2/identity.ini")

def sprawdz_token(token,service_name):
    response = None
    i = identity[service_name.upper()]

    if not i['access_token']:
        print("Pierwsza autoryzacja")
        okno()
        return
    if not i['refresh_token']:
        print("Pierwsza autoryzacja")
        okno()
        return

    if service_name == 'twitch':
        url = identity[service_name.upper()]['uri']  + "validate"
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url,headers=headers)

    elif service_name == 'spotify' :
        try:
            headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
            }
            url = "https://api.spotify.com/v1/me/player/currently-playing"
            response = requests.get(url,headers=headers)
            #There is no API endpoint for checking whether the access token is still valid. Usually you would store 
            #it along with the expires_in value that tells you until when it is valid.
            #An alternative is making a request to any endpoint from the Web API passing the access token. 
            #You will get a 401 Unauthorized status code back if the token has expired.
        except:
            pass 
    identity.read("Oauth2/identity.ini")
    if  response.status_code == 401:
        json = webhook.refresh(service_name)
        response = requests.get(url,headers=headers)
        if response.status_code == 401 and i['access_token'] == "":
            print("Pierwsza autoryzacja")
            okno()
    else:
        try:
            print(f"Token ważny jeszcze przez {round((response.json().get('expires_in'))/3600,2)}godz")
        except:
            print("cos poszlo nie tak: ",response.content," kod ",response.status_code)
            
        return True




#----------------------------------------------------------------------------------------


wsh = comclt.Dispatch("WScript.Shell")
ap = comclt.Dispatch("Shell.Application")
class Bot(commands.Bot):
#logowanie do IRC    
    def __init__(self):
        super().__init__(token=ACCESS_TOKEN, prefix = PREFIX, initial_channels=INITIAL_CHANNELS)  
            
    async def event_ready(self):
        print(f'Zalogowano jako {self.nick}')
        # print(f'user ID {self.user_id}')
        
#powitanie po właczeniu i wejsciu na kanał
    async def event_channel_joined(self,channel):    
        # await channel.send(f"Bążur @{channel.name}!")
        pass
    
#logowanie eventu dołączania viewerów (wtf)
    async def event_join(self,channel,user):
        with open("viewers.log","a") as log:
            log.write(f"{datetime.now()} Stream @{channel.name} User: {user.name}\n")
    @commands.command(name = "drop")
    async def drop(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name} wyrzucił broń LUL')
        komendy.valorant.drop(ctx)
    @commands.command(name = "ping")
    async def ping(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author} pingnął KEKW')
        komendy.valorant.ping(ctx)
    @commands.command(name = "notepad")
    async def notepad(self, ctx:commands.Context):
        komendy.valorant.notepad(ctx)
    @commands.command(name = "allchat")
    async def allchat(self, ctx:commands.Context):
        komendy.valorant.allchat(ctx)
    @commands.command(name = "teamchat")
    async def teamchat(self, ctx:commands.Context):
       komendy.valorant.teamchat(ctx)
    @commands.command(name = "knife")
    async def knife(self,ctx:commands.Context):
           komendy.valorant.knife(ctx)
    @commands.command(name = "pulpit")
    async def pulpit(self,ctx:commands.Context):
        komendy.valorant.pulpit(ctx)
    @commands.command(name = "thank")
    async def thank(self,ctx:commands.Context):
        komendy.valorant.thank(ctx)
    @commands.command(name = "skill")
    async def skill(self,ctx:commands.Context):
        komendy.valorant.skill(ctx)
    @commands.command(name = "song")
    async def song(self,ctx:commands.Context):
        await ctx.send(getCurrentlyPlaying(identity['SPOTIFY']['access_token']))
    @commands.command(name = "shutdown")
    async def shutdown(self,ctx:commands.Context):
        komendy.valorant.shutdown(ctx)
    @commands.command(name = "rotate")
    async def rotate(self,ctx:commands.Context):
        p = multiprocessing.Process(target = komendy.valorant.rotate)
        p.start()
    @commands.command(name = "idzpan")
    async def idzpan(self,ctx:commands.Context):
        p = multiprocessing.Process(target = komendy.valorant.idzpan)
        p.start()
    @commands.command(name = "myszka")
    async def myszka(self,ctx:commands.Context):
        komendy.valorant.myszka()



    @commands.command(name = "bits")
    async def bits(self,ctx:commands.Context):
        config.read("zmienne.ini")
        menu = "**Menu bitsow ©** --------------------"
        linebreak = "______________________________"
        for nazwa in config["VALBITSY"]: 
            if config["BITSY"][nazwa] == "1": 
                menu = menu+nazwa+"-"+config["VALBITSY"][nazwa]+" | "
    @commands.command(name = "komendy", aliases=["commands", "help"])
    async def komendy(self,ctx:commands.Context):
        x = "$allchat <tekst> - napisz wiadomość w grze na /all || $drop - wyrzuć broń || $knife - wyjmij kose || $notepad <tekst> - otworz notatnik i wpisz <tekst> || $ping - Ping w grze || $pulpit - zminimalizuj WSZYSTKIE okna || $skill <q,c,e> - użyj jednego ze skilli, podając przycisk || $song - nazwa piosenki || $teamchat <tekst> - napisz coś w grze na /team || $thank - thank the bus driver || $bits - lista włączonych komend na bitsy || $shutdown - wyłącz komputer za 100 sekund" 
        await ctx.send(x)
    #wyślij liste komend do zmienne.ini




    def update_komendy(self):
        print("MAIN >> Update komendy")
        sekcje = ["KOMENDY", "POINTSY", "BITSY", "VALPOINTSY", "VALBITSY"]
        config.read("zmienne.ini")
        if not config.sections() == sekcje:
                open("zmienne.ini","w")
                print("MAIN >> Config Pusty, tworze nowy")
                sekcjeConfig = config.sections()
                for sekcja in sekcje:
                    if sekcja not in sekcjeConfig:
                        config.add_section(sekcja)
                print("MAIN >> Stworzono sekcje")

        for command in self.commands.values():
                #dodawanie komend
            if not command.name in config["KOMENDY"]:   
                config['KOMENDY'][command.name] = "0"
                print(f"MAIN >> Dodaje komendę {command.name}...")
                config['POINTSY'][command.name] = "0"
                config['BITSY'][command.name] = "0"
                config['VALPOINTSY'][command.name] = "0"
                config['VALBITSY'][command.name] = "0"
                #usuwanie komend
            for konfigkomenda in config["BITSY"]:
                if not konfigkomenda in self.commands:
                    del config["BITSY"][konfigkomenda] 
            for konfigkomenda in config["POINTSY"]:
                if not konfigkomenda in self.commands:
                    del config["POINTSY"][konfigkomenda] 
            for konfigkomenda in config["KOMENDY"]:
                if not konfigkomenda in self.commands:
                    del config["KOMENDY"][konfigkomenda] 
            for konfigkomenda in config["VALPOINTSY"]:
                if not konfigkomenda in self.commands:
                    del config["VALPOINTSY"][konfigkomenda] 
            for konfigkomenda in config["VALBITSY"]:
                if not konfigkomenda in self.commands:
                    del config["VALBITSY"][konfigkomenda] 
                


        with open('zmienne.ini', 'w') as plik:
            config.write(plik)


    async def event_message(self, message = twitchio.Message):
        config.read("zmienne.ini")
        c = config["KOMENDY"]
        #print(message.raw_data) #debug wiadomosci
        if message.echo: #ignoruj samego siebie
            return
        else:
            if message.content.startswith("$"):
                cmd_name = message.content.split(" ")[0][1:]  #komenda bez prefixu
                if cmd_name not in c.keys():
                    return
                elif c[cmd_name] == "1":
                    print("MAIN >> Komenda "+cmd_name+" od "+message.author.display_name)
                    await self.handle_commands(message)
                else:
                    # Send a message or do nothing if the command is disabled
                    await message.channel.send(f"Komenda ${cmd_name} jest wyłączona")
            else:
                # Process regular messages
                await self.handle_commands(message)
    


#------------------------------- PROCESY 
webhookProcess = multiprocessing.Process(target=wlacz_webhook)
sshProcess = multiprocessing.Process(target=ssh.config_sync)
tokenRefreshProcess = multiprocessing.Process(target=webhook.background_token_refresh)
pointbitsProcess = multiprocessing.Process(target=pointbits)



#-------------------------------

#inicjalizacja komendą python main.py
if __name__ == "__main__":
    
    webhookProcess.start()
    sprawdz_token(user_token,'twitch')
    sprawdz_token(identity['SPOTIFY']['access_token'],'spotify')
    bot = Bot()
    bot.update_komendy()
    ssh.execute()
    sshProcess.start()
    tokenRefreshProcess.start()
    pointbitsProcess.start()
    print(f"Logowanie do kanalu {INITIAL_CHANNELS[0]}...")
    bot.run()
    

    
    
    

    
