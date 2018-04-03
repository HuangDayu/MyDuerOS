import mqtt.mymqtt
import time

topic = 'DuerOS_LED'

while True:
    time.sleep(2000)
    mqtt.mymqtt.myclient.publish(topic, str(time.time()))