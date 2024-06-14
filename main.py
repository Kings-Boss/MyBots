import telegram

# Replace with your bot's token obtained from BotFather
bot_token = "6344064287:AAHLrjamkrCGEN4kDzRARvJQfFKFR6gt_BI"

def echo(update, context):
  # Get the user's message text
  user_message = update.message.text
  
  # Send the same message back to the user
  context.bot.send_message(chat_id=update.effective_chat.id, text=user_message)

def main():
  # Initialize the bot with the token
  updater = telegram.Updater(token=bot_token)
  dispatcher = updater.dispatcher

  # Add a handler for messages
  dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, echo))

  # Start the bot
  updater.start_polling()
  updater.idle()

if __name__ == "__main__":
  main()
