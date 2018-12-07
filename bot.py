import discord, json, asyncio, requests
from discord.ext.commands import Bot


currencies = ['BTC-ACM','BTC-AEON', 'BTC-ARQ', 'BTC-BBS', 'BTC-BCN', 'BTC-BCN', 'BTC-BKC', 'BTC-BLOC', 'BTC-BSM', 'BTC-BTCP', 'BTC-CIV']

help_text = 
'''
    !btc{TICKER} - Gives Price, High, Low , and Asking price of inputed Ticker.



'''

def getPrice(currency, crypto):


url = "https://tradeogre.com/api/v1/ticker/BTC-ACM"
response = requests.get(url)
data = response.json()

btc_acm_price = data['price']
btc_acm_high = data['high']
btc_acm_low = data['low']

print(btc_acm_price + '\n'+ btc_acm_high + '\n'+  btc_acm_low)
'''
client = Bot(command_prefix = "$")
btc_acm_high
TOKEN = ""

@client.event
async def on_ready():
    print("Logged in")


@client.command()
async def price():
    url = "https://tradeogre.com/api/v1/markets"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)

    btc_acm_price = parsed["BTC-ACM"]["price"]


    




client.run(TOKEN)
'''