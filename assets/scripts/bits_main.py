from twitchio.ext import pubsub
import main
import asyncio
import twitchio


class bitbot():
        async def main():
            user_token="dji7vy3dlc0szw4vz28ai6cllt4p9b"
            client = twitchio.Client(token = user_token)
            await client.start()    
            @client.event()
            async def event_channel_joined():
                print("jjj")
client.loop.run_until_complete(main())