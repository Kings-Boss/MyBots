const TelegramBot = require('telegraf');

const token = '6344064287:AAHLrjamkrCGEN4kDzRARvJQfFKFR6gt_BI';

const bot = new TelegramBot(token, { polling: true });

bot.on('text', (msg) => {
  const text = msg.text;
  bot.telegram.sendMessage(msg.chat.id, text);
});

console.log('Bot is running...');
