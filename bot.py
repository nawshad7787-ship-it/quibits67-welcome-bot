import os
import random
from telegram import Update
from telegram.ext import Application, ChatMemberHandler, ContextTypes

WELCOME_MESSAGES = [
    "⚛️ Welcome to Qubits-67 — Your Physics Era Begins Here!",
    "🌌 Welcome to the Quantum Side!",
    "🧠 Welcome, Future Physicist!",
    "⚡ Another mind enters the Physics Zone!",
    "💀 Another one joins the struggle against Physics.",
    "🚀 Welcome to Qubits-67 — Let the Physics Begin!"
]

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    member = update.chat_member.new_chat_member

    if member.status == "member":
        await update.effective_chat.send_message(
            random.choice(WELCOME_MESSAGES)
        )

TOKEN = os.environ["BOT_TOKEN"]

app = Application.builder().token(TOKEN).build()

app.add_handler(
    ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER)
)

app.run_polling()
