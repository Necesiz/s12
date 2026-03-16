import asyncio
import os

# Lazımi kitabxanaların olub-olmadığını yoxlayırıq
try:
    import pyrogram
    import telethon
except ImportError:
    print("Sistemdə lazımi kitabxanalar tapılmadı. Yüklənir...")
    os.system("pip3 install pyrogram==1.4.16 telethon tgcrypto")

from pyrogram import Client
from telethon import TelegramClient
from telethon.sessions import StringSession

async def main():
    print("\n--- RikoUB Universal Sessiya Qurucu ---")
    print("1. Pyrogram v1 (Userbotlar üçün ən stabildir)")
    print("2. Pyrogram v2 (Yeni botlar üçün)")
    print("3. Telethon")
    
    secim = input("\nSeçiminizi edin (1, 2 və ya 3): ")
    
    api_id = int(input("API ID daxil edin: "))
    api_hash = input("API HASH daxil edin: ")

    if secim == "1":
        print("\n--- [ PYROGRAM v1 SESSİYASI ] ---")
        async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
            string = await app.export_session_string()
            print(f"\n✅ Sizin String (v1):\n\n{string}\n")
            
    elif secim == "2":
        # Əgər v2 lazımdırsa, pip-lə yeniləmək lazımdır, amma v1 skripti ilə də v2 almaq olar
        print("\n--- [ PYROGRAM v2 SESSİYASI ] ---")
        async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
            string = await app.export_session_string()
            print(f"\n✅ Sizin String (v2):\n\n{string}\n")
            
    elif secim == "3":
        print("\n--- [ TELETHON SESSİYASI ] ---")
        async with TelegramClient(StringSession(), api_id, api_hash) as client:
            string = client.session.save()
            print(f"\n✅ Sizin String (Telethon):\n\n{string}\n")
            
    else:
        print("❌ Yanlış seçim!")

if __name__ == "__main__":
    asyncio.run(main())
