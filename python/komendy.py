import main
import win32api
import win32con
import win32com.client as comclt
import configparser
import time
wsh = comclt.Dispatch("WScript.Shell")
ap = comclt.Dispatch("Shell.Application")

class valorant():
    
    def allchat(ctx):
        wsh.SendKeys("1")
        time.sleep(0.3)
        wsh.SendKeys("g")
    def ping(ctx):
        wsh.SendKeys("z")  
    def notepad(ctx):
        wsh.Run("notepad.exe") 
        time.sleep(0.2)
        wsh.SendKeys("LOL LOL LOL LOL LOL LOL LOL LOL LOL LOL LOL LOL LOL ")
    def allchat(ctx):
        msg = (ctx.message.content)
        msg = msg.replace("$allchat","")
        wsh.SendKeys("{Enter}")
        time.sleep(0.05)
        wsh.SendKeys("{/}")
        wsh.SendKeys("all")
        time.sleep(0.05)
        wsh.SendKeys(msg)
        wsh.SendKeys("{Enter}")
    def teamchat(ctx):
        msg = (ctx.message.content)
        msg = msg.replace("$teamchat","")
        wsh.SendKeys("{Enter}")
        time.sleep(0.05)
        wsh.SendKeys("{/}")
        wsh.SendKeys("team")
        time.sleep(0.05)
        wsh.SendKeys(msg)
        wsh.SendKeys("{Enter}")
    def knife(ctx):
        wsh.SendKeys("3") 
    def pulpit(ctx):
        ap.ToggleDesktop()
    def thank(ctx):
        wsh.SendKeys(".")
        time.sleep(0.05)
        wsh.SendKeys("31")
    def skill(ctx):
        s = ctx.message.content
        s = s.replace("$skill ", "")
        wsh.SendKeys(s)