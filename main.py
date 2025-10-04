import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

QUIZ = {
    "1+1": "2",
    "မြန်မာနိုင်ငံ တိုင်းဒေသကြီး": "၇",
    "Telegram ကိုဖန်တီးသူ": "Pavel Durov",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("မင်္ဂလာပါ 🎉 Quiz Bot စတင်အသုံးပြုနိုင်ပါပြီ!\n/quiz ဆိုပြီး စမ်းကြည့်ပါ။")

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "မေးခွန်းများ:\n"
    for i, q in enumerate(QUIZ.keys(), 1):
        text += f"{i}. {q}\n"
    text += "\nတုံ့ပြန်ဖို့ /answer <နံပါတ်> <အဖြေ> လို့ရေးပါ"
    await update.message.reply_text(text)

async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("❌ format မှားတယ်: /answer <နံပါတ်> <အဖြေ>")
        return

    q_num = int(context.args[0]) - 1
    user_answer = " ".join(context.args[1:])
    correct_answer = list(QUIZ.values())[q_num]

    if user_answer.lower() == correct_answer.lower():
        await update.message.reply_text("✅ မှန်ပါတယ်! 🎉")
    else:
        await update.message.reply_text(f"❌ မှားပြီ၊ ဖြေမှန်ကတော့ {correct_answer}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quiz", quiz))
    app.add_handler(CommandHandler("answer", answer))
    app.run_polling()

if __name__ == "__main__":
    main()
