import discord
from discord.ext import commands
from discord import app_commands

import asyncio
from config import TOKEN
from ai import gen_text
from user import add

bot = commands.Bot(command_prefix=None, intents=None)

@bot.tree.command(name="gen", description="Сгенерировать ответ по текстовому запросу") 
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.allowed_installs(guilds=True, users=True)
async def _gen(interaction: discord.Interaction, prompt: str):
        add(interaction.user.id, prompt)
        await interaction.response.defer()
        await asyncio.sleep(1)
        result = gen_text(prompt)

        if len(result) > 1999:
            await interaction.followup.send("Привышен лимит символов", ephemeral=True)
            return

        await interaction.followup.send(result)
        
    
@bot.event
async def on_ready():
    activity = discord.Game(name="/gen", type=3)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    await bot.tree.sync()

bot.run(TOKEN)