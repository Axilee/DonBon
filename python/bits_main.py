from twitchio.ext import pubsub
import main
import asyncio
import twitchio

client = twitchio.Client(token = "c3ab8aa609ea11e793ae92361f002671")

class bitbot():
        async def main():
            user_token="dji7vy3dlc0szw4vz28ai6cllt4p9b"
            await client.start()    
            @client.event()
            async def event_channel_joined():
                print("jjj")


client.loop.run_until_complete(main())
