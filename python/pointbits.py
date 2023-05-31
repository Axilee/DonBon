import twitchio
from twitchio.ext import pubsub
import asyncio
import configparser
import requests
import importlib
config = configparser.ConfigParser()
config.read("Oauth2//identity.ini")
identity = config["TWITCH"]
users_channel_id = 104929447
url = f"https://api.twitch.tv/helix/channel_points/custom_rewards?broadcaster_id={str(users_channel_id)}"

#----- requesty do modyfikacji rewardsów
def createReward(title,cost):

    headers = {
        'client-id': identity["client_id"],
        'Authorization': f"Bearer {identity['access_token']}", 
        'Content-Type': "application/x-www-form-urlencoded" 
    }
    data = {
        "title":{title},
        "cost":{cost},
        "background_color":"#000000",
        "is_user_input_required":True
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
    odp = requests.get(url,headers = headers)
    odp = odp.json()
    if title=="NaN":
        for x in odp["data"]:
            print("POINTBITS >> ",x["title"], " ID ", x["id"])
        return odp["data"]
    else:
        for x in odp["data"]:
            if x["title"] == title:
                return x["id"], x["is_enabled"]
            #todo wykryc jak nie znajdzie, moze to zadziala ponizej // update, dziala to ponizej
        return None, None
    

def modifyReward(id,state,title=None):
    config.read("zmienne.ini")
    cost = config["VALPOINTSY"]
    if state == "enable":
        enable = True
    elif state == "disable":
        enable = False
    else:
        return 0
    if title != None: 
        print(f"POINTBITS >> Zmieniam koszt {title}")
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
    print("POINTBITS >> Updating rewards")
    config.read("zmienne.ini")
    komendy = config["POINTSY"]
    cost = config["VALPOINTSY"]
    for x in komendy:
        rid, is_enabled = getReward(x)
        if komendy[x] == "1":  #sprawdź czy włączony w configu
            if not rid: #sprawdź czy juz jest stworzony taki reward
                print("POINTBITS >> creating ",x)
                createReward(x,cost[x])
            else:
                modifyReward(rid,"enable",x) #włącz komendę bo istnieje i ma 1 w konfigu
        if komendy[x] == "0": 
            if rid and is_enabled:              #sprawdz czy jest juz taki reward
                print("POINTBITS >> disabling ",x)
                modifyReward(rid, "disable")
def purge():
    print("PURGE >> PURGING")
    rewards = getReward()
    for reward in rewards:
        deleteReward(reward["id"])

# def updateRewards(): #awaryjnie odkomentować żeby usunac rewardsy zamiast tej funkcji wyżej^
#     config.read("zmienne.ini")
#     komendy = config["POINTSY"]
#     for x in komendy:
#         if komendy[x] == "1":  #sprawdź czy włączony w configu
#             if getReward(x): #sprawdź czy juz jest stworzony taki reward
#                 print("POINTBITS >> creating ",x)
#                 deleteReward(getReward(x))
            
        




#--------- bot
def pointbits():
    
    my_token = 'dji7vy3dlc0szw4vz28ai6cllt4p9b'
    users_oauth_token = identity["access_token"]
    client = twitchio.Client(token=my_token)
    client.pubsub = pubsub.PubSubPool(client)
    updateRewards() #update rewardsow na init

    from komendy import valorant
    klasa = locals().get("valorant")

    @client.event()
    async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
        config.read("zmienne.ini")
        pointsy = config["POINTSY"]
        print("reward hjakis")
        # print(pubsub.PubSubChannelPointsMessage.input)
        if event.reward.title in pointsy:
            class ctx:
                def __init__(self):
                    self.message = message()
            class  message:
                def __init__(self):
                    self.content = event.input
            ctx = ctx()
            funkcja = event.reward.title
            komenda = getattr(klasa,funkcja)
            komenda(ctx)

    async def main():
        topics = [
            pubsub.channel_points(users_oauth_token)[users_channel_id],
            pubsub.bits(users_oauth_token)[users_channel_id]
        ]
        
        await client.pubsub.subscribe_topics(topics)
        await client.start()
        

    client.loop.run_until_complete(main())