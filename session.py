import asyncio
from pyrogram import Client
from telethon import TelegramClient
from telethon.sessions import StringSession

async def generate_sessions():
    print("\n--- RikoUB Sessiya Qurucu (Pyrogram v1 & Telethon) ---")
    
    try:
        api_id = int(input("1. API ID daxil edin: "))
        api_hash = input("2. API HASH daxil edin: ")
    except ValueError:
        print("❌ Səhv: API ID rəqəm olmalıdır!")
        return

    print("\n--- [ PYROGRAM SESSİYASI ] ---")
    try:
        async with Client(":memory:", api_id=api_id, api_hash=api_hash) as pyro:
            pyro_str = await pyro.export_session_string()
            print(f"\n✅ Sizin PYROGRAM String Session (Kopyalayın):\n\n{pyro_str}\n")
    except Exception as e:
        print(f"❌ Pyrogram xətası: {e}")

    print("-" * 40)

    print("\n--- [ TELETHON SESSİYASI ] ---")
    try:
        async with TelegramClient(StringSession(), api_id, api_hash) as tele:
            tele_str = tele.session.save()
            print(f"\n✅ Sizin TELETHON String Session (Kopyalayın):\n\n{tele_str}\n")
    except Exception as e:
        print(f"❌ Telethon xətası: {e}")

    print("--- PROSES BİTDİ ---")

if __name__ == "__main__":
    asyncio.run(generate_sessions())
