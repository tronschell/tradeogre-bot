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
#Tradeogre prices
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

#Personal API prices
@client.command()
async def sat():
    url2 = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response2 = requests.get(url2)
    data2 = response2.text
    parsed2 = json.loads(data2)
    usd_parsed_btc = parsed2["bpi"]["USD"]["rate"]
    eur_parsed_btc = parsed2["bpi"]["EUR"]["rate"]

    url = "https://gntf7hd0uj.execute-api.us-east-2.amazonaws.com/default/satoshiAPI"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    eur_rate = parsed["EUR"]
    usd_rate = parsed["USD"]

    usd_price = "$ `" +usd_rate + "`\n"
    eur_price = "€ `" +eur_rate + "`\n"

    btc_usd_price = "$ `" + usd_parsed_btc+ "`\n"
    btc_eur_price = "€`" + eur_parsed_btc+ "`\n"

    data = "SAT/USD: "+ usd_price + "SAT/EUR: "+ eur_price + "BTC/USD: " + btc_usd_price + "BTC/EUR: " + btc_eur_price

    embed = discord.Embed(title="Satoshi Price Data", description=data, color =0xff66cc)
    await client.say(embed=embed)

#Satoshi Calculator USD
@client.command()
async def satusd(number, number2):
    url = "https://gntf7hd0uj.execute-api.us-east-2.amazonaws.com/default/satoshiAPI"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    usd_rate = parsed["USD"]
    int_usd_rate = float(usd_rate)

    inputed_price = int(number)
    inputed_amount = int(number2)
    price = inputed_amount*inputed_price
    final_price = format(price*int_usd_rate, '.2f')

    await client.say('$'+str(final_price))

#Satoshi Calculator EUR
@client.command()
async def sateur(number, number2):
    url = "https://gntf7hd0uj.execute-api.us-east-2.amazonaws.com/default/satoshiAPI"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    eur_rate = parsed["EUR"]
    int_eur_rate = float(eur_rate)

    inputed_price = int(number)
    inputed_amount = int(number2)
    price = inputed_amount*inputed_price
    final_price = format(price*int_eur_rate, '.2f')
    
    await client.say('€'+str(final_price))

@client.command()
async def donate():
    await client.say("To donate please use this BTC address: 3CuYbCWtKdW6PqZHHF1oJjpmeX5Ddp6SrV ")

@client.command()
async def api():
    await client.say("We are using the public Tradeogre API: https://tradeogre.com/api/v1")


client.run(os.environ.get('TOKEN', None))
