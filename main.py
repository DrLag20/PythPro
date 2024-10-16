import discord
from discord.ext import commands
import random
from bot_settings import settings

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def ayuda(ctx):
    await ctx.send("Los comandos disponibles son: [!ayuda], muestra los comandos disponibles.")
    await ctx.send("[!bolsa], dice cuánto tiempo tarda una bolsa de plástico en descomponerse.")
    await ctx.send("[!botella], dice cuánto tiempo tarda una botella de plástico en descomponerse.")
    await ctx.send("[!plato], dice cuánto tiempo tarda un plato de plástico en descomponerse.")
    await ctx.send("[!cepillo], dice cuánto tiempo tarda un cepillo de dientes en descomponerse.")
    await ctx.send("[!sorbete], dice cuánto tiempo tarda un sorbete de plástico en descomponerse.")
    await ctx.send("[!cubiertos], dice cuánto tiempo tardan los cubiertos de plástico en descomponerse.")
    await ctx.send("[!tapa], dice cuánto tiempo tarda una tapa de plástico en descomponerse.")

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
