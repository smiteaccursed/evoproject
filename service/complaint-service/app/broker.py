from kombu import Exchange, Queue, Connection

class botqueue():
    def __init__(self, ampq_dsn, exchange_name = "telegram_bot", queue_name="queue", exchange_type='direct'):
        self.dsn = ampq_dsn
        self.callbacks = []
        self.exchange = Exchange(exchange_name, type=exchange_type)
        self.queue = Queue(queue_name, exchange=self.exchange, routing_key=queue_name)

    def send_message(self, message):
        print(self.dsn)
        with Connection(self.dsn) as connection:
            producer = connection.Producer()
            producer.publish(message, exchange=self.exchange, routing_key=self.queue.routing_key)