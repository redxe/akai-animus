import os
import aiohttp
import discord
from discord.ext import commands
from dotenv import load_dotenv

from help.descriptions import FACT, get_random_heading
from networking.info import API_NINJA_URL, BOTLIBRE_URL


load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
API_NINJA_TOKEN = os.getenv('API_NINJA_TOKEN')
BOTLIBRE_ID = os.getenv('BOTLIBRE_APPLICATION_ID')

bot = commands.Bot(command_prefix=".")


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.event
async def on_error(event, *args, **kwargs):
    with open('logs/err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
            return
        raise


@bot.command(name=FACT.name, help=FACT.help)
async def get_fact(ctx):
    headers = {"X-Api-Key": API_NINJA_TOKEN}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(API_NINJA_URL) as response:
            facts = await response.json()
            fact = facts[0]["fact"]
            embed = discord.Embed(title=get_random_heading(FACT), description=fact, color=discord.Color.blue())
            await ctx.send(embed=embed)


@bot.command(name="akai")
async def chat(ctx, *args):
    message = ' '.join(args).replace("\"", "\\\"")
    headers = {'Content-Type': 'application/json'}
    data = '{"application": "%s", "instance": "165", "message": "%s"}' % (BOTLIBRE_ID, message)
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(BOTLIBRE_URL, data=data.__str__()) as response:
            response = await response.json()
            await ctx.send(response["message"].replace("Brain Bot", "Akai Animus"))


if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
