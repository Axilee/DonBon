import twitchio
from twitchio.ext import pubsub
import asyncio
import configparser

def pointbits():
    config = configparser.ConfigParser()
    config.read("Oauth2//identity.ini")
    identity = config["TWITCH"]

    my_token = 'dji7vy3dlc0szw4vz28ai6cllt4p9b'
    users_oauth_token = identity["access_token"]
    users_channel_id = 104929447
    client = twitchio.Client(token=my_token)
    client.pubsub = pubsub.PubSubPool(client)


    @client.event()
    async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
        print("reward?")
        if event.reward.title == "Bążur":
            print("Bążur wydane")
        else:
            print(event.reward.title)


    async def main():
        topics = [
            pubsub.channel_points(users_oauth_token)[users_channel_id],
            pubsub.bits(users_oauth_token)[users_channel_id]
        ]
        await client.pubsub.subscribe_topics(topics)
        await client.start()
        

    client.loop.run_until_complete(main())
#TODO tworzenie rewardsów i usuwanie ich przy wlaczeniu/wylaczeniu komendy za nagrode, wykombinowac jak dodawac/usuwac nagrody za bitsy bez marnowania ich