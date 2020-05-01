import paho.mqtt.client as mqtt

mqttc = mqtt.Client()

# YOU NEED TO CHANGE THE IP ADDRESS OR HOST NAME
mqttc.connect("192.168.0.23")
#mqttc.connect("localhost")

mqttc.loop_start()

mqttc.publish("hello/world", "Hello")

mqttc.loop_stop()

mqttc.disconnect()
