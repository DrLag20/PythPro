import discord
from discord.ext import commands
import random
import os
from bot_settings import settings

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def ayuda(ctx):
    img_name = "comandos.png"
    with open(f'Comandos/{img_name}', 'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def bolsa(ctx):
    await ctx.send("Una bolsa de plástico tarda aproximadamente 10 a 20 años en descomponerse.")

@bot.command()
async def botella(ctx):
    await ctx.send("Una botella de plástico tarda aproximadamente 450 años en descomponerse.")

@bot.command()
async def plato(ctx):
    await ctx.send("Un plato de plástico tarda aproximadamente entre 100 y 1000 años en descomponerse.")

@bot.command()
async def cepillo(ctx):
    await ctx.send("Un cepillo de plástico tarda aproximadamente 500 años en descomponerse.")

@bot.command()
async def sorbete(ctx):
    await ctx.send("Un sorbete de plástico tarda aproximadamente 200 años en descomponerse.")

@bot.command()
async def cubiertos(ctx):
    await ctx.send("Unos cubiertos de plástico (cucharas, tenedores...) tardan aproximadamente 400 a 1000 años en descomponerse.")

@bot.command()
async def tapa(ctx):
    await ctx.send("Una tapa de plástico tarda aproximadamente 150 a 300 años en descomponerse.")

bot.run(settings["TOKEN"])
