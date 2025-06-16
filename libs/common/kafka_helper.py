from kafka import KafkaProducer
import json

def get_kafka_producer(bootstrap_servers="kafka:9092"):
    return KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

def publish_event(topic, event, producer=None):
    if producer is None:
        producer = get_kafka_producer()
    producer.send(topic, event)
    producer.flush()
