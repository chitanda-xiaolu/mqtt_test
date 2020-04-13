# #paho(publisher)
#
# import paho.mqtt.client as mqtt
# import time
# import sys
#
# #定义当与broker连接后的回调函数
# def on_connect(client, userdata, flags, rc):
#     print('Connected with result code' + str(rc))
#
# #定义当发布mqtt信息时的回调函数
# def on_publish(client, userdata, mid):
#     print('Publish topic')
#
# #设定回调函数
# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_publish = on_publish
#
# #与broker建立连接
# client.connect('iot.elipse.org', 1883, 60)
#
# while True:
#     try:
#         client.publish('topic', payload)
#         time.sleep(5)
#     except KeyboardInterrupt:
#         print('EXIT')
#         client.disconnect()
#         sys.exit(0)

# import paho.mqtt.client as mqtt
# import time
# import sys
# import random
#
# def on_connect(client, userdata, flags, rc):
#     print('Connected with result code ' + str(rc))
#
# def on_publish(client):
#     print('temperature')
#
# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_publish = on_publish
#
# client.connect('127.0.0.1', 1883, 60)
#
# while True:
#     try:
#         data = random.randint(24, 28)
#         client.publish('temperature', str(data) + '℃')
#         time.sleep(5)
#     except KeyboardInterrupt:
#         print('EXit')
#         client.disconnect()
#         sys.exit(0)

import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

# data = {'statu': False}
payload = 'status1false'
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("114.55.33.165", 1883, 60)
# 发布 test主题
client.publish("switch", payload)


