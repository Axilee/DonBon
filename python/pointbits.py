import twitchio
from twitchio.ext import pubsub
import asyncio
import configparser
import requests
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
        "background_color":"#000000"
    }
    odp = requests.post(url,headers = headers, data = data)


def deleteReward(id):
    headers = {
        'client-id': identity["client_id"],
        'Authorization': f"Bearer {identity['access_token']}", 
        'Content-Type': "application/x-www-form-urlencoded" 
    }
    data = {
        "title":"game analysis 1v1",
        "cost":100,
        "id":id
    }
    odp = requests.delete(url,headers = headers, data = data)
    print(f"usuwam{id}")


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
    else:
        for x in odp["data"]:
            if x["title"] == title:
                return x["id"], x["is_enabled"]
            #todo wykryc jak nie znajdzie, moze to zadziala ponizej // update, dziala to ponizej
        return None, None
    

def modifyReward(id,state):
    if state == "enable":
        enable = True
    elif state == "disable":
        enable = False
    else:
        return 0
    headers = {
        'client-id': identity["client_id"],
        'Authorization': f"Bearer {identity['access_token']}", 
        'Content-Type': "application/x-www-form-urlencoded" 
    }
    data = {
        "is_enabled": {enable}
    }
    urlid = url + "&id=" + id 
    odp = requests.patch(urlid,headers = headers, data = data)


def updateRewards():
    config.read("zmienne.ini")
    komendy = config["POINTSY"]
    for x in komendy:
        rid, is_enabled = getReward(x)
        if komendy[x] == "1":  #sprawdź czy włączony w configu
            if not rid: #sprawdź czy juz jest stworzony taki reward
                print("POINTBITS >> creating ",x)
                createReward(x,700)
            else:
                modifyReward(rid,"enable") #włącz komendę bo istnieje i ma 1 w konfigu
        if komendy[x] == "0": 
            print (rid, is_enabled)
            if rid and is_enabled:              #sprawdz czy jest juz taki reward
                print("POINTBITS >> disabling ",x)
                modifyReward(rid, "disable")
                    
    
# def updateRewards(): #awaryjnie odkomentować żeby usunac rewardsy zamiast tej funkcji wyżej^
#     for x in komendy:
#         if komendy[x] == "1":  #sprawdź czy włączony w configu
#             if getReward(x): #sprawdź czy juz jest stworzony taki reward
#                 print("POINTBITS >> creating ",x)
#                 deleteReward(getReward(x))
            
        




#--------- bot
def pointbits():
    updateRewards()
    getReward()
    my_token = 'dji7vy3dlc0szw4vz28ai6cllt4p9b'
    users_oauth_token = identity["access_token"]
    client = twitchio.Client(token=my_token)
    client.pubsub = pubsub.PubSubPool(client)
    






    @client.event()

    async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
        print(event)
        if event.reward.title == "Bążur":
            print("Bążur wydane")
        else:
            print(event.reward.id)
        


    async def main():
        topics = [
            pubsub.channel_points(users_oauth_token)[users_channel_id],
            pubsub.bits(users_oauth_token)[users_channel_id]
        ]
        
        await client.pubsub.subscribe_topics(topics)
        await client.start()
        

    client.loop.run_until_complete(main())
#TODO tworzenie rewardsów i usuwanie ich przy wlaczeniu/wylaczeniu komendy za nagrode, wykombinowac jak dodawac/usuwac nagrody za bitsy bez marnowania ich