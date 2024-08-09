import paho.mqtt.client as mqtt
import time
import random


def simulate_temperature():
    """
    Simulate a temperature reading.
    The temperature will fluctuate between 20.0B0C and 30.0B0C.
    """
    return round(random.uniform(20.0, 30.0), 2)


def publish_temperature(client, topic):
    temperature = simulate_temperature()
    print(f"Publishing temperature: {temperature}B0C to topic: {topic}")
    client.publish(topic, temperature)


if __name__ == "__main__":
    broker = "mqtt.eclipse.org"  # Use "localhost" if you're running Mosquitto locally
    topic = "hotel/temperature"
    client = mqtt.Client()
    client.connect(broker)

    while True:
        publish_temperature(client, topic)
        time.sleep(60)
