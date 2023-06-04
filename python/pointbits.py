import twitchio
from twitchio.ext import pubsub
import asyncio
import configparser
import requests
import time
import importlib


config = configparser.ConfigParser()
config.read("Oauth2//identity.ini")
identity = config["TWITCH"]
users_channel_id = 104929447
url = f"https://api.twitch.tv/helix/channel_points/custom_rewards?broadcaster_id={str(users_channel_id)}"
inputrequired_commands = ['allchat','teamchat','notepad','skill']

#----- requesty do modyfikacji rewardsów
def createReward(title,cost,inputrequired):
    if int(cost) == 0: cost = 1 #bo nie da sie nagrody za 0 miec
    headers = {
        'client-id': identity["client_id"],
        'Authorization': f"Bearer {identity['access_token']}", 
        'Content-Type': "application/x-www-form-urlencoded" 
    }
    data = {
        "title":{title},
        "cost":{cost},
        "background_color":"#000000",
        "is_user_input_required": inputrequired
    }
    odp = requests.post(url,headers = headers, data = data)


def deleteReward(id):
    headers = {
        'client-id': identity["client_id"],
        'Authorization': f"Bearer {identity['access_token']}", 
        'Content-Type': "application/x-www-form-urlencoded" 
    }
    data = {
        "id":id
    }
    odp = requests.delete(url,headers = headers, data = data)
    print(f"POINTBITS >> usuwam {id}")


def getReward(title="NaN"):
    headers = {
        'client-id': identity["client_id"],
        'Authorization': f"Bearer {identity['access_token']}", 
        'Content-Type': "application/x-www-form-urlencoded" 
    }
    data = {
        'only_manageable_rewards': True
    }
    odp = requests.get(url,headers = headers)
    odp = odp.json()
    if title=="NaN":
        for x in odp["data"]:
            print("POINTBITS >> ",x["title"], " ID ", x["id"])
        return odp["data"]
    else:
        for x in odp["data"]:
            if x["title"] == title:
                return x["id"], x["is_enabled"], x["cost"]
            #todo wykryc jak nie znajdzie, moze to zadziala ponizej // update, dziala to ponizej
        return None, None, None
    

def modifyReward(id,state=None,title=None):
    config.read("zmienne.ini")
    cost = config["VALPOINTSY"]
    if state == "enable":
        enable = True
    elif state == "disable":
        enable = False
    else:
        enable = None
    if title != None: 
        points = cost[title]
    else: points = ""
    headers = {
        'client-id': identity["client_id"],
        'Authorization': f"Bearer {identity['access_token']}", 
        'Content-Type': "application/x-www-form-urlencoded" 
    }
    data = {
        "is_enabled": {enable},
        "cost": {points} 
    }
    urlid = url + "&id=" + id 
    odp = requests.patch(urlid,headers = headers, data = data)


def updateRewards():
    config.read("zmienne.ini")
    komendy = config["POINTSY"]
    cost = config["VALPOINTSY"]
    for x in komendy:
        if x in inputrequired_commands:
            inputrequired = True
        else:
            inputrequired = False
        rid, is_enabled, getCost = getReward(x)


        # print(x, komendy[x], rid, is_enabled, getCost, cost[x]) #debug
        if komendy[x] == "0": 
            if rid and is_enabled:              #sprawdz czy jest juz taki reward
                print("POINTBITS >> disabling ",x)
                modifyReward(rid, "disable", x)

        if komendy[x] == "1":  #sprawdź czy włączony w configu
            if not rid: #sprawdź czy NIE istnieje ten reward na twtichu
                print("POINTBITS >> creating ",x)
                createReward(x,cost[x],inputrequired)

            elif is_enabled == False:
                print("POINTBITS >> Enabling ",x)
                modifyReward(rid,"enable",x) #włącz komendę bo istnieje i ma 1 w konfigu

            elif int(cost[x]) != int(getCost): #sprawdz czy koszt z configu jest taki sam jak koszt na twitchu
                print(f"POINTBITS >> Zmieniam koszt {x} z {getCost} na {cost[x]}")
                modifyReward(rid,None,x)

        
def purge():
    print("PURGE >> PURGING")
    rewards = getReward()
    for reward in rewards:
        deleteReward(reward["id"])




#--------- bot
def pointbits():
    my_token = '160g7wv175m4mjwzfpd071k5ww8pvx'
    users_oauth_token = identity["access_token"]
    client = twitchio.Client(token=my_token)
    client.pubsub = pubsub.PubSubPool(client)
    print("POINTBITS >> Joining Client")
    updateRewards() #uptade na init odrazu
    
    from komendy import valorant
    klasa = locals().get("valorant")
#REWARDS
    @client.event()
    async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
        config.read("zmienne.ini")
        pointsy = config["POINTSY"]
        # print(pubsub.PubSubChannelPointsMessage.input)
        if event.reward.title in pointsy:
            class ctx: #definiowanie ctx.message bo z komend taki przesyla czasami, wiec tu niech tez bedzie
                def __init__(self):
                    self.message = message()
            class message:
                def __init__(self):
                    self.content = event.input
            ctx = ctx()
            print("POINTBITS >> Channel Points ",event.reward.title)
            funkcja = event.reward.title
            komenda = getattr(klasa,funkcja)
            komenda(ctx)
#BITS
    @client.event()
    async def event_pubsub_bits(event: pubsub.PubSubBitsMessage):
        config.read("zmienne.ini")
        BitRewards = config['VALBITSY']
        print("POINTBITS >> Event bitsy, ilosc="+str(event.bits_used)+" od "+str(event.user.name)+"   "+str(event.message.content))
        msg = str(event.message.content)
        try: 
            msg = msg.split(" ", 1)[1]
        except:
            msg = msg
        class ctx: #definiowanie ctx.message bo z komend taki przesyla czasami, wiec tu niech tez bedzie
                def __init__(self):
                    self.message = message()
        class message:
                def __init__(self):
                    self.content = msg
        ctx = ctx()

        for BitReward in BitRewards:
            if event.bits_used == int(BitRewards[BitReward]):
                if config['BITSY'][BitReward] == "1":
                    print (BitReward)
                    komenda = getattr(klasa,BitReward)
                    komenda(ctx)

                
    async def main():
        topics = [
            pubsub.channel_points(users_oauth_token)[users_channel_id],
            pubsub.bits(users_oauth_token)[users_channel_id]
        ]
        await client.pubsub.subscribe_topics(topics)
        await client.start()
        

    client.loop.run_until_complete(main())