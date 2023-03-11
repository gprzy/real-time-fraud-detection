from kafka import KafkaProducer
import json

class FraudDetectionProducer:
    def __init__(self, bootstrap_servers=['localhost:9092']):
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    def send_to_topic(self, topic_name, message):
        self.producer.send(topic_name, json.dumps(message).encode('utf-8'))
        self.producer.flush()
