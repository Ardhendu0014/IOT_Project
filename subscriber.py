import paho.mqtt.client as mqtt
import sqlite3
import time

THRESHOLD = 25.0
DURATION = 5

def on_message(client, userdata, msg):
    temperature = float(msg.payload.decode())
    timestamp = time.time()

    conn = sqlite3.connect('temperature_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS temperature (timestamp REAL, value REAL)''')
    cursor.execute('INSERT INTO temperature (timestamp, value) VALUES (?, ?)', (timestamp, temperature))
    conn.commit()

    cursor.execute('SELECT value FROM temperature ORDER BY timestamp DESC LIMIT ?', (DURATION,))
    last_values = cursor.fetchall()
    if len(last_values) == DURATION and all(value[0] > THRESHOLD for value in last_values):
        print("ALARM: Temperature has exceeded the threshold for 5 consecutive minutes!")
    
    conn.close()

if __name__ == "__main__":
    broker = "mqtt.eclipse.org"  # Use "localhost" if you're running Mosquitto locally
    topic = "hotel/temperature"

    client = mqtt.Client()
    client.on_message = on_message
    client.connect(broker)
    client.subscribe(topic)
    
    client.loop_forever()
