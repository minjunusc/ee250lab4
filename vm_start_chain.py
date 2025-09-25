# Minjun Kim
# GitHub Repo: https://github.com/minjunusc/ee250lab4
import paho.mqtt.client as mqtt
import socket
import time



def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("minjun/pong")
    client.message_callback_add("minjun/pong", on_message_from_pong)


def on_message_from_pong(client, userdata, message):
   print("Received the integer: "+ message.payload.decode())
   #increase the integer by 1
   increased_num = int(message.payload.decode()) + 1
   time.sleep(1)
   client.publish("minjun/ping", increased_num)

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(host='192.169.0.121', port=1883, keepalive=60)
    
    client.loop_start()
    time.sleep(1)
    print("Publishing an int")
    client.publish("minjun/ping", 67)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    


       
