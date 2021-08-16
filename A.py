import discord
import selenium
import requests
from discord.ext import commands


client = commands.Bot(command_prefix='!')


token ='ODc1NzUxNzc1MjcyMDU0ODA1.YRaFZQ.dGQgU1myHDxKkaKiZZVmDtuMYQE'


@client.event
async def on_ready():
    print("실행 됐노 이기야 이거슨 춤추는샵주가 첨으로 만든 봇이노 이기")


@client.event
async def on_message(message):
    if message.author.bot :
        return

    if message.content.startswith('시발'):
        await message.delete()
        await message.author.send("욕은 안댕")
    
    if message.content.startswith('씨발'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('ㅅㅂ'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('ㅆㅂ'):
        await message.delete()
        await message.author.send("욕은 안댕")
        
    if message.content.startswith('시1발'):
        await message.delete()
        await message.author.send("욕은 안댕")   

    if message.content.startswith('씨1발'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('좆까'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('조까'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('ㅈㄲ'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('새기'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('새끼'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('느금마'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('느그어미'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('느그애미'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('너네엄마'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('애미'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('애비'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('느개비'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('느그애비'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('좆'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('ㅈ'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('ㅈㄴ'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('좆나'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('존나'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('장애'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('장애인'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('장애인아'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('씹'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('ㅆ'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('너거메'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('너거매'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('ㅗ'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('ㅗㅗ'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('ㅗㅗㅗ'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('ㅗㅗㅗㅗ'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('니애미'):
        await message.delete()
        await message.author.send("욕은 안댕")
            
    if message.content.startswith('니엄마'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('운지'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('예아'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('북딱'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('북 딱'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('딱'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('노무'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('이기'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('운지'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('노무현'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('노무딱'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('노알라'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('병신'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('고아'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('좆장애'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('섹스'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('보지'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('ㅅㅅ'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('자지'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('ㅈㅈ'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('ㅂㅈ'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('걸레'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('개색'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('조건만남'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('조건 만남'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('창녀'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('창년'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('씹'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('ㅈ'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('ㅗㅗㅗㅗㅗㅗ'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('ㅗㅗㅗㅗ'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('ㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗ'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('ㅗㅗㅗㅗㅗㅗㅗㅗ'):
        await message.delete()
        await message.author.send("욕은 안댕")
                    
    if message.content.startswith('ㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗ'):
        await message.delete()
        await message.author.send("욕은 안댕")

    
client.run(token)