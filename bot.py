import discord
from discord.ext import commands
from datetime import datetime
from colorama import Fore
from discord.voice_client import VoiceClient
import time

def get_time():
	return ('\033[1m' + Fore.LIGHTMAGENTA_EX + datetime.now().strftime("%H:%M:%S") + Fore.WHITE)

prefix = ">"
acc_token = "token bro"
bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
	print(f"{get_time()}{Fore.LIGHTGREEN_EX} [+] Bot started")

@bot.command(pass_context=True)
async def musiclist(ctx):
	await ctx.send("*[+] List: monkey, scare, pokemon, daddy, malamala, golagola, pustinogu, phintro, najlonkesa*")

@bot.command(pass_context=True)
async def play(ctx, music: str = None):
	if music == None:
		await ctx.send(f"** [X] Usage: {prefix}play [MUSIC] | Use {prefix}musiclist to see all available music. |**")
	elif music == "scare":

		await ctx.send("[+] Sound executing...")
		print(f"{get_time()}{Fore.WHITE} [+] Sound executing...")
		channel = ctx.message.author.voice.channel
		print(f"{get_time()}{Fore.WHITE} [+] Getting the channel...")
		vc = await channel.connect()
		print(f"{get_time()} [+] Connected to the channel")
		print(f"{get_time()} [+] Playing the sound...")
		vc.play(discord.FFmpegPCMAudio('music\\sound.mp3'))
		while vc.is_playing():
			time.sleep(1)
		await vc.disconnect()
		print(f"{get_time()} [+] Left the channel")
		print(f"{get_time()} {Fore.LIGHTGREEN_EX} [+] Sucessfuly pranked")
	elif music == "monkey":
		await ctx.send("[+] Sound executing...")
		print(f"{get_time()}{Fore.WHITE} [+] Sound executing...")
		channel = ctx.message.author.voice.channel
		print(f"{get_time()}{Fore.WHITE} [+] Getting the channel...")
		vc = await channel.connect()
		print(f"{get_time()} [+] Connected to the channel")
		print(f"{get_time()} [+] Playing the sound...")
		vc.play(discord.FFmpegPCMAudio('music\\monkey.mp3'))
		while vc.is_playing():
			time.sleep(1)
		await vc.disconnect()
		print(f"{get_time()} [+] Left the channel")
		print(f"{get_time()} {Fore.LIGHTGREEN_EX} [+] Sucessfuly pranked")
	elif music == "pokemon":
		await ctx.send("[+] Sound executing...")
		print(f"{get_time()}{Fore.WHITE} [+] Sound executing...")
		channel = ctx.message.author.voice.channel
		print(f"{get_time()}{Fore.WHITE} [+] Getting the channel...")
		vc = await channel.connect()
		print(f"{get_time()} [+] Connected to the channel")
		print(f"{get_time()} [+] Playing the sound...")
		vc.play(discord.FFmpegPCMAudio('music\\pokemon.mp3'))
		while vc.is_playing():
			time.sleep(1)
		await vc.disconnect()
		print(f"{get_time()} [+] Left the channel")
		print(f"{get_time()} {Fore.LIGHTGREEN_EX} [+] Sucessfuly pranked")
	elif music == "daddy":
		await ctx.send("[+] Sound executing...")
		print(f"{get_time()}{Fore.WHITE} [+] Sound executing...")
		channel = ctx.message.author.voice.channel
		print(f"{get_time()}{Fore.WHITE} [+] Getting the channel...")
		vc = await channel.connect()
		print(f"{get_time()} [+] Connected to the channel")
		print(f"{get_time()} [+] Playing the sound...")
		vc.play(discord.FFmpegPCMAudio('music\\daddy.mp3'))
		while vc.is_playing():
			time.sleep(1)
		await vc.disconnect()
		print(f"{get_time()} [+] Left the channel")
		print(f"{get_time()} {Fore.LIGHTGREEN_EX} [+] Sucessfuly pranked")
	elif music == "najlonkesa":
		await ctx.send("[+] Sound executing...")
		print(f"{get_time()}{Fore.WHITE} [+] Sound executing...")
		channel = ctx.message.author.voice.channel
		print(f"{get_time()}{Fore.WHITE} [+] Getting the channel...")
		vc = await channel.connect()
		print(f"{get_time()} [+] Connected to the channel")
		print(f"{get_time()} [+] Playing the sound...")
		vc.play(discord.FFmpegPCMAudio('music\\najlonkesa.mp3'))
		while vc.is_playing():
			time.sleep(1)
		await vc.disconnect()
		print(f"{get_time()} [+] Left the channel")
		print(f"{get_time()} {Fore.LIGHTGREEN_EX} [+] Sucessfuly pranked")
	elif music == "golagola":
		await ctx.send("[+] Sound executing...")
		print(f"{get_time()}{Fore.WHITE} [+] Sound executing...")
		channel = ctx.message.author.voice.channel
		print(f"{get_time()}{Fore.WHITE} [+] Getting the channel...")
		vc = await channel.connect()
		print(f"{get_time()} [+] Connected to the channel")
		print(f"{get_time()} [+] Playing the sound...")
		vc.play(discord.FFmpegPCMAudio('music\\golagola.mp3'))
		while vc.is_playing():
			time.sleep(1)
		await vc.disconnect()
		print(f"{get_time()} [+] Left the channel")
		print(f"{get_time()} {Fore.LIGHTGREEN_EX} [+] Sucessfuly pranked")
	elif music == "pustinogu":
		await ctx.send("[+] Sound executing...")
		print(f"{get_time()}{Fore.WHITE} [+] Sound executing...")
		channel = ctx.message.author.voice.channel
		print(f"{get_time()}{Fore.WHITE} [+] Getting the channel...")
		vc = await channel.connect()
		print(f"{get_time()} [+] Connected to the channel")
		print(f"{get_time()} [+] Playing the sound...")
		vc.play(discord.FFmpegPCMAudio('music\\pustinogu.mp3'))
		while vc.is_playing():
			time.sleep(1)
		await vc.disconnect()
		print(f"{get_time()} [+] Left the channel")
		print(f"{get_time()} {Fore.LIGHTGREEN_EX} [+] Sucessfuly pranked")
	elif music == "malamala":
		await ctx.send("[+] Sound executing...")
		print(f"{get_time()}{Fore.WHITE} [+] Jumpscare executing...")
		channel = ctx.message.author.voice.channel
		print(f"{get_time()}{Fore.WHITE} [+] Getting the channel...")
		vc = await channel.connect()
		print(f"{get_time()} [+] Connected to the channel")
		print(f"{get_time()} [+] Playing the sound...")
		vc.play(discord.FFmpegPCMAudio('music\\malamala.mp3'))
		while vc.is_playing():
			time.sleep(1)
		await vc.disconnect()
		print(f"{get_time()} [+] Left the channel")
		print(f"{get_time()} {Fore.LIGHTGREEN_EX} [+] Sucessfuly pranked")
	elif music == "phintro":
		await ctx.send("[+] Sound executing...")
		print(f"{get_time()}{Fore.WHITE} [+] Jumpscare executing...")
		channel = ctx.message.author.voice.channel
		print(f"{get_time()}{Fore.WHITE} [+] Getting the channel...")
		vc = await channel.connect()
		print(f"{get_time()} [+] Connected to the channel")
		print(f"{get_time()} [+] Playing the sound...")
		vc.play(discord.FFmpegPCMAudio('music\\phintro.mp3'))
		while vc.is_playing():
			time.sleep(1)
		await vc.disconnect()
		print(f"{get_time()} [+] Left the channel")
		print(f"{get_time()} {Fore.LIGHTGREEN_EX} [+] Sucessfuly pranked")
	else:
		await ctx.send("** Music not found! **")
#credits
@bot.command(pas_context=True)
async def credits(ctx):
	await ctx.send("[+] Check your console.")
	print(f"{get_time()} "+ Fore.RED + f"Music Selfbot Credits\n- Start Code/Bot by Pera\n- Selfbot Ability, All in one cmd [{prefix}play] by Ivano")


bot.run(acc_token, bot=False)



"""
 Bot Made by Pera || Selfbot + all in one cmd made by ivano!
Bot Made by Pera || Selfbot + all in one cmd made by ivano!
 Bot Made by Pera || Selfbot + all in one cmd made by ivano!
Bot Made by Pera || Selfbot + all in one cmd made by ivano!
 Bot Made by Pera || Selfbot + all in one cmd made by ivano!
Bot Made by Pera || Selfbot + all in one cmd made by ivano!
 Bot Made by Pera || Selfbot + all in one cmd made by ivano!
Bot Made by Pera || Selfbot + all in one cmd made by ivano!
 Bot Made by Pera || Selfbot + all in one cmd made by ivano!
Bot Made by Pera || Selfbot + all in one cmd made by ivano!
 Bot Made by Pera || Selfbot + all in one cmd made by ivano!
Bot Made by Pera || Selfbot + all in one cmd made by ivano!
"""
