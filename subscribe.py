import paho.mqtt.client as mqtt
import json


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # 连接时订阅test主题
    client.subscribe("statu")


def on_message(client, userdata, msg):
    print(msg.topic + "： " + str(msg.payload) + str(type(msg.payload)))
    print(eval(str(msg.payload)[1::]))
    client.disconnect()


client = mqtt.Client()
client.connect("114.55.33.165", 1883, 60)
client.subscribe("statu")
# client.on_connect = on_connect
client.on_message = on_message
# client.connect("127.0.0.1", 1883, 60)
client.loop_forever()