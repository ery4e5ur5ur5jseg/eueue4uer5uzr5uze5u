import discord
from discord.ext import commands
from discord import Client, Intents, Embed

bot = commands.Bot(command_prefix="!", case_insensitive=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("yes")

@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Vulanty | Help Menu", description = "Showing every command | Prefix is !", color = 0xFFFFF)

    em.add_field(name = "N/A", value = "**N/A**")

    em.add_field(name = "N/A", value = "**N/A**")

    await ctx.send(embed = em)

@bot.command()
async def test(ctx):
  await ctx.send("Test!")

bot.run("ODgxODg5NDA1NDAzNTU3OTY5.YSzZgg.Mg1F832IyNLu4H0CDTU3MDlUYFo")
