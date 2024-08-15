from pyrogram import Client, filters
from pyrogram.types import Message

api_id = 14960174
api_hash = "7200e9b88534a2101fc8657af3677b38"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

status = "online"

@app.on_message(filters.me & filters.command("status", prefixes="."))
async def change_status(client: Client, message: Message):
    global status
    cmd = message.text.split(" ", 1)
    if len(cmd) > 1:
        status = cmd[1].lower()
        await message.reply_text(f"Статус изменен на {status}")

@app.on_message(filters.private & ~filters.me)
async def auto_reply(client: Client, message: Message):
    if status == "offline":
        await message.reply_text(f"👋 Привет {message.from_user.first_name}.\n\n❌ Сейчас я оффлайн.")
    elif status == "online":
        await message.reply_text(f"👋 Привет {message.from_user.first_name}.\n\n✅ Сейчас я онлайн, ждите ответ.")

app.run()