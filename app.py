# bot.py
import os
import requests

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

all_tokens = requests.get("https://api.coingecko.com/api/v3/coins/list")
all_tokens_json = all_tokens.json()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{client.user} has connected to Discord!')

    async def on_message(self, message):
        if message.author == self.user.id:
            return
            

        if message.content.lower().startswith("/p") or message.content.lower().startswith("/price"):
            print(message.content)
            print(message.content.split())
            symbol = message.content.split()[1]
            index = next((i for i, item in enumerate(all_tokens_json) if item["symbol"] == symbol), None)

            if index != None:
                id = all_tokens_json[index]["id"]
                name = all_tokens_json[index]["name"]
                
                response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=php,usd".format(all_tokens_json[index]["id"]))
                response_json = response.json()
                price = "{:,.8f}".format(response_json[id]["usd"]).rstrip("0").rstrip(".") 
                php = "{:,.8f}".format(response_json[id]["php"]).rstrip("0").rstrip(".") 

                bot_message = "Name:\t{}\nSymbol:\t{}\nPrice:\t{} USD\nPhp:\t{} PHP".format(name, symbol.upper(), price, php)

                await message.reply(bot_message, mention_author=False)

            else:
                await message.reply("Unknown coin. Baka na typo ka bobo.", mention_author=False)

client = MyClient()
client.run(TOKEN)