import logging
import config

from kombu import Message
from time import sleep
from broker import botqueue

import telebot
# setup logging
logger = logging.getLogger("telegram-notify-service")
logging.basicConfig(
    level=logging.INFO,            
    format="[%(levelname)s][%(name)s][%(filename)s, line %(lineno)d]: %(message)s"
)
app_config: config.Config = config.load_config(_env_file='.env')
bot=telebot.TeleBot(app_config.TELEGRAM_BOT_TOKEN.get_secret_value());
tque = botqueue(app_config.RABBITMQ_DSN.unicode_string())
    
def process_message(body, message: Message):
    logger.info(f"Recieved message {message} with content: {body}")
    print(body)
    try:
        for uid in app_config.TELEGRAM_USER_IDS:
            bot.send_message(chat_id=uid, text=body)
            print(f"Сообщение отправлено пользователю с ID {uid}")
    finally:
        message.ack()
tque.register_callback(process_message)

if __name__ == "__main__":
    while True:
        try:
            tque.run_consumer()
        except KeyboardInterrupt:
            logger.info("Keyboard interrupt. Exiting...")
            break
        except Exception as e:
            logger.error(f"Connection error: {str(e)}. Retrying in 5 seconds...")
            sleep(5)

