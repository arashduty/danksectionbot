from discord.ext import commands

bot = commands.Bot(command_prefix="!d")

@bot.event
async def on_ready():
    print(f"Logged in!\nUsername: {bot.user.name}\n ID: {bot.user.id}\n Guilds: {len(bot.guilds)}")

@bot.command()
async def say(ctx, *, args):
    await ctx.send(args)

bot.run("NzM2NTU2NTAxNTczMDQyMjU3.Xxwhsg.7_GEF5E0bYAa2XcLzS-44icjTFa")
