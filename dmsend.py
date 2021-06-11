import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('★마인★')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.guild_permissions.manage_messages:
                        embed = discord.Embed(color=0x1DDB16, timestamp=message.created_at)
                        embed.add_field(name="★★테스트★★", value=msg, inline=True)
                        embed.set_footer(text="★마인 보냄 ㅋ★")
                        await i.send(embed=embed)
                except:
                    pass


client.run('ODUyNzc3MzE0MzIzMzk4NjU3.YMLwww.IeuBSBHDzH7M-kE0j1TjcxfCeIo')
