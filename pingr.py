import discord
import asyncio

TOKEN = 'ur token (dont remove the quotes from this)'
CHANNEL_ID = "the channel u want to ping it in (remove the quotes from this)"
USER_ID = "the user u want to spam ping (remove the quotes from this too)"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel("the channel u want to ping it in (remove the quotes from this)")
    if channel is None:
        channel = await client.fetch_channel(CHANNEL_ID)

    while True:
        try:
            await channel.send(f"<@{USER_ID}> Ping!")
            print("Mention sent!")
        except discord.HTTPException as e:
            print(f"Failed to send message: {e}")
        await asyncio.sleep(0.1)  # Sleep for 0.1 seconds

client.run('ur token (dont remove the quotes from this)')
