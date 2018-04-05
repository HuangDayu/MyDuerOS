import paho.mqtt.client as mqtt
import sys
import uuid
import time

broker = '183.230.40.39'
port = 6002
username = '102504'
password = 'gaLr=XxjhVGMf1=t4qazdJA6Nmk='
clientid = '28319870'
topic = 'DuerOS_LED'

def on_connect(client, userdata, null,rc):
    print('Connected. Client id is: ' + clientid)
    client.subscribe(topic)
    print('Subscribed to topic: ' + topic)

    client.publish(topic, 'Message from Baidu IoT demo')
    print('MQTT message published.')

def on_message(client, userdata, msg):
    msg = str(msg.payload)#, 'ISO-8859-1'
    print('MQTT message received: ' + msg)
    if msg == 'exit':
        sys.exit()

client = mqtt.Client(clientid)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username, password)

print('Connecting to broker: ' + broker)
client.connect(broker, port)
myclient = client
client.loop_forever()