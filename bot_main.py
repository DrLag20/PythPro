from bot_settings import settings 
import discord
# import * - es una forma rápida de importar todos los archivos de la biblioteca
from bot_logic import gen_emodji, flip_coin, gen_pass

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)


# Una vez que el bot esté listo, ¡imprimirá su nombre!
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# Cuando el bot reciba un mensaje, ¡enviará mensajes en el mismo canal!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('¡Hola! Soy un bot')
    elif message.content.startswith('$help'):
        await message.channel.send('Comandos disponibles: [$help], el bot proporciona la lista de comandos disponibles.')
        await message.channel.send('[$smile], el bot reacciona con un emoji sonriente.')
        await message.channel.send('[$coin], el bot selecciona uno de los dos lados de la moneda.')
        await message.channel.send('[$pass], el bot genera una contraseña de 10 dígitos.')
        await message.channel.send('[$userinfo], el bot proporciona información del usuario.')
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$userinfo'):
        user_id = message.author.id
        user = await client.fetch_user(user_id)
        await message.channel.send(f'Usuario: {user.name} , id: {user.id}')
    else:
        await message.channel.send("No puedo procesar este comando, lo siento!")

client.run(settings["TOKEN"])
