import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot je Online")
    
@client.command()
async def trovo(ctx,korisnik=None):
    if korisnik == None:
        await ctx.reply("Nisi upisao strimera!")
        return
    try:
        headers= {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}
        response = requests.get('https://trovo.live/'+korisnik,headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        Naslov = soup.find('h3').get_text().strip()
        Kategorija = soup.find(class_='link mr10').get_text().strip()
        Ime = soup.find(class_='streamer-name text-overflow').get_text().strip()
        Jezik = soup.find(class_='flex-auto text-overflow tag-name').get_text().strip()

        embed = discord.Embed(title=f'',description=f'Ime: `{Ime}`\nKategorija: `{Kategorija}`\nJezik: `{Jezik}`',color = discord.Color(0x17ff00))
        embed.set_author(name=f"{Naslov}",icon_url="https://cdn.discordapp.com/attachments/872603079248338984/914554276834058340/trovo.png")
        await ctx.reply(embed=embed)
    except:
        await ctx.reply('Korisnik nije pronadjen.')

client.run('TOKEN')