from kombu import Exchange, Queue, Connection, Consumer
import logging 
from socket import timeout as tout

logger = logging.getLogger("telegram-service")


class botqueue():
    def __init__(self, ampq_dsn, exchange_name = "telegram_bot", queue_name="queue", exchange_type="direct"):
        self.dsn = ampq_dsn
        self.callbacks = []
        self.exchange = Exchange(exchange_name, type=exchange_type)
        self.queue = Queue(queue_name, exchange=self.exchange, routing_key=queue_name)
    
    def register_callback(self, callback):
        self.callbacks.append(callback)

    def send_message(self, message):
        with Connection(self.dsn) as connection:
            producer = connection.Producer()
            producer.publish(message, exchange=self.exchange, routing_key=self.queue.routing_key)

    def run_consumer(self):
        with Connection(self.dsn) as connection:
            with connection.Consumer(self.queue, callbacks=self.callbacks) as consumer:
                logger.info("Started pooling messages")
                while True:
                    try:
                        connection.drain_events(timeout=10)
                    except tout:
                        connection.heartbeat_check()