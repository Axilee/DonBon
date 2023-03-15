import twitchio
import asyncio
from twitchio.ext import pubsub

my_token = "dji7vy3dlc0szw4vz28ai6cllt4p9b"
users_oauth_token = "uc6wftw4zvot86y7o8t3wga6d2gnt7"
users_channel_id = 161307951
client = twitchio.Client(token=my_token)
client.pubsub = pubsub.PubSubPool(client)

@client.event()
async def event_pubsub_bits(event: pubsub.PubSubBitsMessage):
    print('bitsy')

@client.event()
async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
    if event.reward.id == "2f445287-bff8-401b-8011-e44e070c60ca":
        print('Odebrano wspólny wypad w gierce')
    else:
        print(f'Użytkownik {event.channel_id} odebrał {event.reward} o ID = {event.id}, jego input {event.input}, status {event.status}')

async def main():
    topics = [
        pubsub.channel_points(users_oauth_token)[users_channel_id],
        pubsub.bits(users_oauth_token)[users_channel_id]
    ]
    await client.pubsub.subscribe_topics(topics)
    await client.start()

client.loop.run_until_complete(main())

