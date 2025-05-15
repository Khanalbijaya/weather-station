import sqlite3
import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    client.subscribe("sensor/dht11")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    data = json.loads(payload)
    temperature = float(data['temperature'])
    humidity = float(data['humidity'])
    
    conn = sqlite3.connect('sensor_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO data (temperature, humidity) VALUES (?, ?)", (temperature, humidity))
    conn.commit()
    conn.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
