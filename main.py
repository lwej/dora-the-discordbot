import discord
import secrets
from discord.ext import commands
import pi_display as pi

# Fetch discord token
TOKEN = secrets.token()

# Create bot object with special command prefix
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_message(message):
    if message.content == "hello":
        mention = message.author.mention
        await message.channel.send("Hello " + mention + "!")

    await bot.process_commands(message)


@bot.command(
    help="If you ever need a boost, y'know",
    brief="Displays an encouraging message <3"
)
async def boost(ctx):
    await ctx.channel.send(secrets.affirmation_of_the_day())


@bot.command(
    help="Type !kiwi followed by the message you want to bother them with. (Max 32 characters)",
    brief="Sends something to a display in Kiwi's home."
)
async def kiwi(ctx, *args):
    response = ""

    for arg in args:
        response = response + " " + arg

    # Unique case:
    # Bot runs on rPi zero with an LCD display
    if pi.send_msg(response):
        await ctx.channel.send(response + " was successfully sent to Kiwi :) ")
    else:
        await ctx.channel.send(response + " couldn't be sent to Kiwi :( ")


def main():
    bot.run(TOKEN)


if __name__ == '__main__':
    main()
