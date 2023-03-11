from kafka import KafkaConsumer
import requests
import json
from producer import FraudDetectionProducer

producer = FraudDetectionProducer()

consumer = KafkaConsumer('fraud_detection_requests',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         group_id='fraud_detection_group')

model_url = 'http://localhost:5002/fraud_detection'

for message in consumer:
    message_data = json.loads(message.value.decode('utf-8'))

    headers = {'Content-type': 'application/json'}
    response = requests.post(model_url, data=json.dumps(message_data), headers=headers)
    result = json.loads(response.content.decode('utf-8'))

    producer.send_to_topic('fraud_detection_results', result)
