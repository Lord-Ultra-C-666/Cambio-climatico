import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

from actions import get_action

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# 🌍 Impacto global (vive mientras el bot esté encendido)
impacto_total = 0


@bot.event
async def on_ready():
    print(f"Conectado como {bot.user} 💚")


@bot.command()
async def accion(ctx):
    global impacto_total
    impacto_total += 1

    action = get_action()

    await ctx.send(
        f"🌱 **Acción ecológica del día:**\n"
        f"**{action}**\n\n"
        f"📌 Impacto total de hoy: **{impacto_total}**"
    )


@bot.command()
async def impacto(ctx):
    await ctx.send(
        f"🌍 **Impacto de la comunidad hoy**\n\n"
        f"🧴 Botellas de plástico salvadas: **{impacto_total}**\n"
        f"💚 Cada acción cuenta"
    )


@bot.command(name="eco_meme")
async def eco_meme(ctx):
    memes = [
        "🌳 Planta un árbol o te juzgo silenciosamente 👀",
        "🌍 El planeta te vio tirar basura… y no está orgulloso 😔",
        "♻️ Reciclar es sexy, no hacerlo no 😤",
        "🐢 Las tortugas creen en ti… no las decepciones",
        "💚 El medio ambiente te manda un abrazo (por ahora)"
    ]
    await ctx.send(random.choice(memes))


@bot.command(name="eco_help")
async def eco_help(ctx):
    await ctx.send(
        "💚 **EcoBot – Comandos disponibles** 🌍\n\n"
        "🌱 `!accion` → Acción ecológica + suma impacto\n"
        "🌍 `!impacto` → Impacto comunitario\n"
        "😂 `!eco_meme` → Meme ecológico random\n"
        "💚 `!eco_help` → Ayuda kawaii\n\n"
        "Gracias por cuidar el planeta ✨"
    )


bot.run(TOKEN)
