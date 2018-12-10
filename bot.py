import discord, json, asyncio, requests, os
from discord.ext.commands import Bot


primaryCurrency = ['BTC', 'LTC']

altCoin = ['ACM','AEON', 'ARQ', 'BBS', 'BCN', 'BKC', 'BLOC', 'BSM', 'BTCP', 'CIV',
'COAL', 'D', 'DASH', 'DERO', 'DOGE', 'ETH', 'ETN', 'ETNX', 'ETNXP', 'FBF', 'GPKR', 'GRFT',
'INC', 'INTU', 'IRD', 'KRB', 'LNS', 'LOKI', 'LTC', 'LTHN', 'LUX', 'MSR', 'NAH', 'NBR', 'OMB',
'PCN', 'PIVX', 'PIVX', 'PLURA', 'PURK', 'QTUM', 'QUAN', 'RTO', 'RVN', 'RYO', 'SHB', 'SLD', 'SOLACE',
'SUMO', 'SUQA', 'TRTL', 'TUBE', 'WAE', 'WOW', "WTIP", 'XAO', 'XGS', 'XHV', 'XMC', 'XMR', 'XMV', 
'XNV', 'XPP', 'XRN', 'XTA', 'XTL', 'XTRI', 'XUN', 'XVG', 'ZEL']

client = Bot(command_prefix = "!")



@client.event
async def on_ready():
    print("Logged in")


@client.command()
async def price(currency, crypto):

    input1 = str(currency.upper())
    input2 = str(crypto.upper())

    if(input1 in primaryCurrency):
        if(input2 in altCoin):
            url = "https://tradeogre.com/api/v1/ticker/{}-{}".format(input1, input2)
            response = requests.get(url)
            data = response.json()

            price_data = data['price']
            high_data = data['high']
            low_data = data['low']
                
            finalString = "Current Price: " + str(price_data) + '\n' +"24hr High: " + str(high_data) + '\n' + "24hr Low: " + str(low_data)

            embed = discord.Embed(title='{}-{}'.format(input1, input2), description=finalString, color =0x00ff00)

            await client.say(embed=embed)
        else:
            await client.say("Not a supported currency pair")
    else:
        await client.say("Not a supported currency pair")

@client.command()
async def donate():
    await client.say("To donate please use this BTC address: 3CuYbCWtKdW6PqZHHF1oJjpmeX5Ddp6SrV ")

@client.command()
async def api():
    await client.say("We are using the public Tradeogre API: https://tradeogre.com/api/v1")


client.run(os.environ.get('TOKEN', None))
