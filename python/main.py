import os
import time
import asyncio
from datetime import datetime
from twitchio.ext import commands
from twitchio import Message
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
#wczytaj konfig zmienne.ini
config = configparser.ConfigParser()
zmienne = config.read("zmienne.ini")
identity = configparser.ConfigParser()
identityFile = identity.read("Oauth2/identity.ini")

user_token = identity['TWITCH']['access_token'] #zaczyt tokenu auth dla twitch
refresh_token = identity['TWITCH']['refresh_token'] #imo lepiej tutac execowac refresh token bedzie latwiej go responsem odnawiac 
client_id = identity["TWITCH"]['client_id']
client_secret = identity["TWITCH"]['client_secret']
#ewentualnie odczyt/zapis konfiguracji co godzine a generowanie tokenu gdzie indziej



#dane połączenia

ACCESS_TOKEN = 'dji7vy3dlc0szw4vz28ai6cllt4p9b'

PREFIX = "$"

INITIAL_CHANNELS=["aaxile"]




#--------------------------------------GLOBALNE FUNKCJE ---------------------------------
#sprawdz status komendy z zmienne ini
def sprawdz(typ,nazwa):
    config.get(typ, nazwa)

def wlacz_webhook():
            httpd = make_server('localhost',5000,initWebhook.webhook.flaskAppWebhook.app)
            httpd.serve_forever()
def okno():
        initWebhook.inicjalizuj.wybor()
webhookProcess = multiprocessing.Process(target=wlacz_webhook)

def sprawdz_token(token):
    headers = {'Authorization': f'Bearer {token}'}
    url = 'https://id.twitch.tv/oauth2/validate'
    response = requests.get(url,headers=headers)
    if response.status_code == 401:
        webhook.flaskAppWebhook.refresh("twitch",refresh_token,client_id,client_secret)
    else:
        print(f"Token ważny jeszcze przez {round((response.json().get('expires_in'))/3600,2)}godz")
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
        await channel.send(f"Bążur @{channel.name}!")
    
#logowanie eventu dołączania viewerów (wtf)
    async def event_join(self,channel,user):
        with open("viewers.log","a") as log:
            log.write(f"{datetime.now()} Stream @{channel.name} User: {user.name}\n")
    @commands.command(name = "drop")
    async def drop(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name} wyrzucił broń LUL')
        wsh.SendKeys("1")
        time.sleep(0.3)
        wsh.SendKeys("g")
    @commands.command(name = "ping")
    async def ping(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author} pingnął KEKW')
        wsh.SendKeys("z")
    @commands.command(name = "cof")
    async def cof(self, ctx: commands.Context):
        wsh.SendKeys("")
    @commands.command(name = "notepad")
    async def notepad(self, ctx:commands.Context):
        wsh.Run("notepad.exe") 
        time.sleep(0.2)
        wsh.SendKeys("LOL")
    @commands.command(name = "allchat")
    async def allchat(self, ctx:commands.Context):
        msg = (ctx.message.content)
        msg = msg.replace("$allchat","")
        wsh.SendKeys("{Enter}")
        time.sleep(0.05)
        wsh.SendKeys("{/}")
        wsh.SendKeys("all")
        time.sleep(0.05)
        wsh.SendKeys(msg)
        wsh.SendKeys("{Enter}")
    @commands.command(name = "teamchat")
    async def teamchat(self, ctx:commands.Context):
        msg = (ctx.message.content)
        msg = msg.replace("$teamchat","")
        wsh.SendKeys("{Enter}")
        time.sleep(0.05)
        wsh.SendKeys("{/}")
        wsh.SendKeys("team")
        time.sleep(0.05)
        wsh.SendKeys(msg)
        wsh.SendKeys("{Enter}")
    @commands.command(name = "knife")
    async def knife(self,ctx:commands.Context):
        wsh.SendKeys("3")    
    @commands.command(name = "pulpit")
    async def pulpit(self,ctx:commands.Context):
        ap.ToggleDesktop()
    @commands.command(name = "thank")
    async def thank(self,ctx:commands.Context):
        wsh.SendKeys(".")
        time.sleep(0.05)
        wsh.SendKeys("31")
    @commands.command(name = "skill")
    async def skill(self,ctx:commands.Context):
        s = ctx.message.content
        s = s.replace("$skill ", "")
        wsh.SendKeys(s)
    @commands.command(name = "czesc")
    async def czesc(self,ctx:commands.Context):
        await ctx.send(user_token)
    #@commands.command(name = "chatgpt")
    #async def chatgpt(self,ctx:commands.Context):



#wyślij liste komend do zmienne.ini
    def update_komendy(self):
        for command in self.commands.values():
            if not config.read("zmienne.ini"):
                open("zmienne.ini","w")
                print("\nKonfig Pusty, tworze nowy")
                config.add_section("KOMENDY")
                print("Stworzono sekcje KOMENDY")
            if not command.name in config["KOMENDY"]:   
                config['KOMENDY'][command.name] = "0"
                print(f"Dodaje komendę {command.name}...")
        with open('zmienne.ini', 'w') as plik:
            config.write(plik)
 


#inicjalizacja komendą python main.py
if __name__ == "__main__":
    print (f"CONFIG: {zmienne}")
    webhookProcess.start()
    if sprawdz_token(user_token):
         pass
    else:
        print("Token expired!")
        okno()
    bot = Bot()
    bot.update_komendy()
    ssh.execute()
    print(f"\nLogowanie do kanalu {INITIAL_CHANNELS[0]}...")
    bot.run()
    
    
    

    
