# bot.py
import os
import requests

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{client.user} has connected to Discord!')

    async def on_message(self, message):
        if message.author == self.user.id:
            return
        
        if message.content.lower().startswith("?p") or message.content.lower().startswith("?price"):
            print(message.content)
            print(message.content.split())
            if message.content.split()[1].lower() == "axs":
                response = requests.get("https://api.coingecko.com/api/v3/simple/token_price/ethereum?contract_addresses=0xbb0e17ef65f82ab018d8edd776e8dd940327b28b&vs_currencies=php")
                response_json = response.json()
                price = response_json["0xbb0e17ef65f82ab018d8edd776e8dd940327b28b"]["php"]
                print(price)

                await message.reply("{} Php per AXS\nSource: CoinGecko".format(price), mention_author=False)
            
            if message.content.split()[1].lower() == "slp":
                response = requests.get("https://api.coingecko.com/api/v3/simple/token_price/ethereum?contract_addresses=0xcc8fa225d80b9c7d42f96e9570156c65d6caaa25&vs_currencies=php")
                response_json = response.json()
                price = response_json["0xcc8fa225d80b9c7d42f96e9570156c65d6caaa25"]["php"]
                print(price)
                
                await message.reply("{} Php per SLP\nSource: CoinGecko".format(price), mention_author=False)

client = MyClient()
client.run(TOKEN)