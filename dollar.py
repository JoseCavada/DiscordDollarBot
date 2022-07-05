import discord
import requests
my_secret = #clave privada de api discord
client = discord.Client()


def valor_dolar():
    resp = requests.get ('https://mindicador.cl/api/dolar')
    datos = resp.json()
    dolar_hoy = datos ['serie'][0]['valor']
    dolar_ayer = datos ['serie'][1]['valor']
    if dolar_hoy > dolar_ayer:
        valor = "El valor del dólar hoy es de: ```CLP$" + str(dolar_hoy) + "```" + "!Dólar al alza!:chart_with_upwards_trend: \n" + "Dólar ayer: ```CLP$" + str(dolar_ayer) + "```"
        return valor
    elif dolar_hoy < dolar_ayer:
        valor = "El valor del dolar hoy es de: ```CLP$" + str(dolar_hoy) + "```" + "!Que el dólar está bajando gente! :chart_with_downwards_trend:\n"+ "Dólar ayer: ```CLP$" + str(dolar_ayer) + "```"
        return valor
    else:
        valor = "El valor del dolar hoy es de ```CLP$" + str(dolar_hoy) + "```" + "Está estable, sin más"
        return valor
  
  





@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$dollar'):
        await message.channel.send(valor_dolar())

    


client.run(my_secret)