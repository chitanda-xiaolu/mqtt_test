import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

# data = {'statu': False}
payload = 'socket1true'
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("114.55.33.165", 1883, 60)
# 发布 test主题
client.publish("switch", payload)