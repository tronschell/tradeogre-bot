import discord, json, asyncio, requests
from discord.ext.commands import Bot


currencies = ['BTC-ACM','BTC-AEON', 'BTC-ARQ', 'BTC-BBS', 'BTC-BCN', 'BTC-BCN', 'BTC-BKC', 'BTC-BLOC', 'BTC-BSM', 'BTC-BTCP', 'BTC-CIV', 'BTC-COAL', 'BTC-D', 'BTC-DASH', 'BTC-DERO', 'BTC-DOGE', 'BTC-ETH', 'BTC-ETN', 'BTC-ETNX', 'BTC-ETNXP', 'BTC-FBF', 'BTC-GPKR', 'BTC-GRFT', 'BTC-INC', 'BTC-INTU', 'BTC-IRD', 'BTC-KRB', 'BTC-LNS', 'BTC-LOKI', 'BTC-LTC', 'BTC-LTHN', 'BTC-LUX', 'BTC-MSR', 'BTC-NAH', 'BTC-NBR', 'BTC-OMB', 'BTC-PCN', 'BTC-PIVX', 'BTC-PIVX', 'BTC-PLURA', 'BTC-PURK', 'BTC-QTUM', 'BTC-QUAN', 'BTC-RTO', 'BTC-RVN', 'BTC-RYO', 'BTC-SHB', 'BTC-SLD', 'BTC-SOLACE', 'BTC-SUMO', 'BTC-SUQA', 'BTC-TRTL', 'BTC-TUBE', 'BTC-WAE', 'BTC-WOW', "BTC-WTIP", 'BTC-XAO', 'BTC-XGS', 'BTC-XHV', 'BTC-XMC', 'BTC-XMR', 'BTC-XMV', 'BTC-XNV', 'BTC-XPP', 'BTC-XRN', 'BTC-XTA', 'BTC-XTL', 'BTC-XTRI', 'BTC-XUN', 'BTC-XVG', 'BTC-ZEL']

client = Bot(command_prefix = "$")
TOKEN = ""

help_text:'''

!price {BTC/LTC}{TICKER} - gives price data including: high, low and current price.
!donate - gives developer Bitcoin address

'''



@client.event
async def on_ready():
    print("Logged in")


@client.command()
async def price(currency, crypto):
    try:
        input1 = currency.upper()
        input2 = crypto.upper()

        if(currency.upper() in currencies):
            url = "https://tradeogre.com/api/v1/ticker/{}-{}".format(input1, input2)
            response = requests.get(url)
            data = response.json()

            btc_acm_price = data['price']
            return btc_acm_price
        else:
            return "Not a supported currency"
    except:
        return "Error"

async def donate():
    client.say("To donate please use this BTC address: ")



client.run(TOKEN)
