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
