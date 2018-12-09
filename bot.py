import discord, json, asyncio, requests
from discord.ext.commands import Bot


yes = ['BTC', 'LTC']

currencies = ['ACM','AEON', 'ARQ', 'BBS', 'BCN', 'BKC', 'BLOC', 'BSM', 'BTCP', 'CIV',
'COAL', 'D', 'DASH', 'DERO', 'DOGE', 'ETH', 'ETN', 'ETNX', 'ETNXP', 'FBF', 'GPKR', 'GRFT',
'INC', 'INTU', 'IRD', 'KRB', 'LNS', 'LOKI', 'LTC', 'LTHN', 'LUX', 'MSR', 'NAH', 'NBR', 'OMB',
'PCN', 'PIVX', 'PIVX', 'PLURA', 'PURK', 'QTUM', 'QUAN', 'RTO', 'RVN', 'RYO', 'SHB', 'SLD', 'SOLACE',
'SUMO', 'SUQA', 'TRTL', 'TUBE', 'WAE', 'WOW', "WTIP", 'XAO', 'XGS', 'XHV', 'XMC', 'XMR', 'XMV', 
'XNV', 'XPP', 'XRN', 'XTA', 'XTL', 'XTRI', 'XUN', 'XVG', 'ZEL']

client = Bot(command_prefix = "!")
TOKEN = "NTIxMTM0ODI5MjE2MDcxNzMw.Du4EOg.ypV2JbmHXg3uAGUozLAI9w3VR98"

help_text:'''

!price {BTC/LTC}{TICKER} - gets current price data including: high, low and current price.
!donate - gives developer Bitcoin address

'''


@client.event
async def on_ready():
    print("Logged in")


@client.command()
async def price(currency, crypto):

    input1 = currency.upper()
    input2 = crypto.upper()

    if(input1 in yes&& input2 in currencies):
        url = "https://tradeogre.com/api/v1/ticker/{}-{}".format(input1, input2)
        response = requests.get(url)
        data = response.json()

        price_data = data['price']
        high_data = data['high']
        low_data = data['low']
            
        finalString = "Current Price: " + price_data + "24hr High: " + high_data + "24hr Low: " + low_data

        embed = discord.Embed(title='{}-{}'.format(currency, crypto), description=finalString, color =0x00ff00)

        await client.say(finalString)
    else:
        await client.say("Test")

@client.command()
async def donate():
    await client.say("To donate please use this BTC address: ")

@client.command()
async def api():
    await client.say("We are using the public Tradeogre API: https://tradeogre.com/api/v1")



client.run(TOKEN)
