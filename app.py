# bot.py
import os
import requests
from random import choice

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

all_tokens = requests.get("https://api.coingecko.com/api/v3/coins/list")
all_tokens_json = all_tokens.json()

unknown_coin = ["Unknown coin.", "Coin not found.", "Invalid coin."]
unknown_coin_2 = ["Baka na typo ka bobo.", "Ayusin mo tanga.", "Gago ka ba? Just asking."]

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{client.user} has connected to Discord!')

    async def on_message(self, message):
        if message.author == self.user.id:
            return
            

        if message.content.lower().startswith("?p") or message.content.lower().startswith("?price"):
            if len(message.content.split()) == 2:

                symbol = message.content.lower().split()[1]
                index = next((i for i, item in enumerate(all_tokens_json) if item["symbol"] == symbol), None)

                if index != None:
                    id = all_tokens_json[index]["id"]
                    name = all_tokens_json[index]["name"]
                    
                    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=php,usd".format(all_tokens_json[index]["id"]))
                    response_json = response.json()
                    price = "{:,.8f}".format(response_json[id]["usd"]).rstrip("0").rstrip(".") 
                    php = "{:,.8f}".format(response_json[id]["php"]).rstrip("0").rstrip(".") 

                    bot_message = "Name:\t{}\nSymbol:\t{}\nPrice:\t{} USD\nPhp:\t{} PHP\nSource:\tCoingecko".format(name, symbol.upper(), price, php)

                    await message.reply(bot_message, mention_author=False)

                else:
                    await message.reply(f"{choice(unknown_coin)} {choice(unknown_coin_2)}", mention_author=False)

            elif len(message.content.split()) == 1:
                await message.reply("Lagyan mo ng coin bobo.")
            
            else:
                await message.reply("Too many parameters. Isa lang uyyy.")

client = MyClient()
client.run(TOKEN)