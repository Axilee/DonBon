import main
import win32api
import win32con
import win32com.client as comclt
import configparser
import time
import rotatescreen
import keyboard
import mouse
import multiprocessing
wsh = comclt.Dispatch("WScript.Shell")
ap = comclt.Dispatch("Shell.Application")

def runProcess(funkcja):
    # funckja = getattr("komendy",funkcja)
    p = multiprocessing.Process(target=funkcja)
    p.daemon=True
    p.start()


class valorant():
    
    def knife(ctx):
        wsh.SendKeys("1")
        time.sleep(0.3)
        wsh.SendKeys("g")
    def ping(ctx):
        wsh.SendKeys("z")  
    def notepad(ctx):
        wsh.Run("notepad.exe") 
        time.sleep(0.2)
        wsh.SendKeys(ctx.message.content.replace("$notepad",""))
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
    def drop(ctx):
        wsh.SendKeys("G")
    def shutdown(ctx):
        win32api.ShellExecute(0,"open","cmd","/C shutdown -s -t 100","",1)
    def rotate(ctx = None):
        main = rotatescreen.get_primary_display()
        main.rotate_to(180)
        time.sleep(10)
        main.rotate_to(0)
    def idzpan(ctx = None):
        endTime = time.time() + 15
        keyboard.block_key("s")
        keyboard.block_key("w")
        while time.time() < endTime:
            keyboard.press("w")
            if not keyboard.is_pressed("w"):
                keyboard.press("w")
            keyboard.release("s")
        keyboard.release("w")
    def myszka(ctx = None):
        for i in range(40):
            mouse.move(-i*i,0,absolute=False,duration=0.1)
            mouse.move(i*i,0,absolute=False,duration=0.1)
        

