import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

litros_por_minuto = 5.5

ideas = [
    "Reutiliza objetos antes de tirarlos. Piensa si pueden tener un nuevo uso.",
    "Recicla adecuadamente: separa los residuos correctamente (papel, plástico, vidrio, orgánico).",
    "Crea compost con desechos orgánicos en lugar de tirarlos a la basura.",
    "Ahorra energía apagando luces cuando no las uses.",
    "Reduce el consumo de agua: toma duchas más cortas y arregla fugas en tu hogar.",
    "Compra productos hechos con materiales reciclados siempre que sea posible.",
    "Utiliza transporte sostenible: camina, usa bicicleta o transporte público en lugar de vehículos privados."
]

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

def calcular_consumo_agua(tiempo_minutos):
    return tiempo_minutos * litros_por_minuto

@bot.command()
async def agua(ctx, tiempo: float):
    consumo = calcular_consumo_agua(tiempo)
    await ctx.send(f"Si dejas la llave abierta por {tiempo} minutos, gastaras aproximadamente {consumo} litros de agua.")

@bot.command()
async def idea(ctx):
    idea_aleatoria = random.choice(ideas)
    await ctx.send(f"💡 Idea para reciclar y reducir la contaminación: {idea_aleatoria}")

bot.run(TOKEN)