from telegram.ext import ApplicationBuilder, MessageHandler, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

async def reply(update, context):
    await update.message.reply_text("✅ البوت شغال الآن 24 ساعة")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
