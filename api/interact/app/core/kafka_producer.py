from kafka import KafkaProducer
import json
from app.core.config import settings

producer = KafkaProducer(
    bootstrap_servers=settings.kafka_bootstrap.split(","),
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def publish(event: dict):
    producer.send(settings.kafka_topic, event)
    producer.flush()
