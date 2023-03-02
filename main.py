import os
import time
import asyncio
from twitchio.ext import commands, pubsub
import win32com.client as comclt
import win32api
import win32con
import configparser


wsh = comclt.Dispatch("WScript.Shell")
ap = comclt.Dispatch("Shell.Application")
ACCESS_TOKEN = 'mdigv4lzgkn7durd4ww44812riy6dk'
PREFIX = "$"
INITIAL_CHANNELS=["Aaxile"]

config = configparser.ConfigParser()
zmienne = config.read("zmienne.ini")
print (f"CONFIG: {zmienne}")
#print (config.sections())



class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=ACCESS_TOKEN, prefix = PREFIX, initial_channels=INITIAL_CHANNELS)    
    
    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        
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
        print (msg)
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
        print (msg)
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
    @commands.command(name = "test")
    async def test(self):
        print (0)
        
    def update_komendy(self):
        d = {}
        for command in self.commands.values():
            print(command.name)
            if not command.name in config["KOMENDY"]:   
                config['KOMENDY'][command.name] = "0"
        with open('zmienne.ini', 'w') as plik:
            config.write(plik)




if __name__ == "__main__":
    bot = Bot()
    bot.update_komendy()
    bot.run()
    