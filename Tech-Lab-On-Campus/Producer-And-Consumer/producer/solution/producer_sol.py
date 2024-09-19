import pika
import os
import sys
from producer_interface import mqProducerInterface

class mqProducer(mqProducerInterface): 
    def __init__(self,routing_key, exchange_name):
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        # call setupMQConnection 
        self.setupRMQConnection()

    def setupRMQConnection(self):
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)
        # Establish Channel
        self.channel = self.connection.channel()
        # Create the exchange if not already present
        self.exchange = self.channel.exchange_declare(exchange="Tech Lab Exchange")

    def publishOrder(self, message: str) -> None:
        # Basic Publish to Exchange
        self.channel.basic_publish(
            exchange="Tech Lab Exchange",
            routing_key="Tech Lab Key",
            body="Message",
        )
        # Close Channel
        self.channel.close()
        # Close Connection
        self.connection.close()