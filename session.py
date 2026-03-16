import asyncio
from pyrogram import Client
from telethon import TelegramClient
from telethon.sessions import StringSession

async def get_pyro_session(api_id, api_hash):
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        print("\n✅ Pyrogram String Sessionunuz:\n")
        print(await app.export_session_string())
        print("\n⚠️ Bunu kopyalayıb config-də PYRO_STRING hissəsinə yazın.")

async def get_tele_session(api_id, api_hash):
    async with TelegramClient(StringSession(), api_id, api_hash) as client:
        print("\n✅ Telethon String Sessionunuz:\n")
        print(client.session.save())
        print("\n⚠️ Bunu kopyalayıb config-də TELE_STRING hissəsinə yazın.")

async def main():
    print("--- RikoUB String Session Generator ---")
    api_id = int(input("API ID: "))
    api_hash = input("API HASH: ")
    
    print("\nHansı stringi almaq istəyirsiniz?")
    print("1. Pyrogram")
    print("2. Telethon")
    choice = input("\nSeçiminiz (1/2): ")
    
    if choice == "1":
        await get_pyro_session(api_id, api_hash)
    elif choice == "2":
        await get_tele_session(api_id, api_hash)
    else:
        print("❌ Yanlış seçim!")

if __name__ == "__main__":
    asyncio.run(main())
