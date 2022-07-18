import discord
import os

TOKEN = ''

client = discord.Client()

#起動時ターミナルに通知
@client.event
async def on_ready():
    print("login success")

@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は処理しない
    if message.author.bot:
        return

    if message.content == "/start":
        await message.channel.send("Server starting up...")
        os.system("gcloud --account=ark-botserver-serviceaccount@ark-hdk.iam.gserviceaccount.com compute instances start ark-instance --project ark-hdk --zone us-west1-b")
        await message.channel.send("起動まで20分程掛かるよ。気長に待ってね。")
    
    if message.content == "/stop":
        await message.channel.send("Server is stopping...")
        os.system("gcloud --account=ark-botserver-serviceaccount@ark-hdk.iam.gserviceaccount.com compute instances stop ark-instance --project ark-hdk --zone us-west1-b")
        await message.channel.send("きちんと停止するまで5分程かかるよ。停止前に起動コマンドを打たないでね。")

    if message.content == '/help':
        await message.channel.send('/start : サーバーの起動')
        await message.channel.send('/stop : サーバーの停止') 


client.run(TOKEN)