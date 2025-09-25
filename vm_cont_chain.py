import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("minjun/ping")
    client.message_callback_add("minjun/ping", on_message_from_ping)

def on_message_from_ping(client, userdata, message):
   print("New integer: "+ message.payload.decode())
   #increase the integer by 1
   increased_num = int(message.payload.decode()) + 1
   time.sleep(1)
   client.publish("minjun/pong", increased_num)


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(host='192.169.0.121', port=1883, keepalive=60)
    client.loop_forever()