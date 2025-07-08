import network, time, dht
from machine import Pin
from umqtt.simple import MQTTClient

# WiFi
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect("SAPTO", "wahyugantengsekali")

print("Connecting to WiFi...", end="")
while not sta.isconnected():
    print(".", end="")
    time.sleep(0.5)
print("\nConnected to WiFi")
print("IP:", sta.ifconfig()[0])

# MQTT setup
mqtt_client_id = "esp32_dht"
mqtt_server = "broker.hivemq.com"
mqtt_topic = "iot/sapto/dht"

client = MQTTClient(mqtt_client_id, mqtt_server)
client.connect()
print("Connected to MQTT broker")

# DHT11 on GPIO 4
sensor = dht.DHT11(Pin(4))

# Loop
while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        msg = "Temp:{}C,Hum:{}%".format(temp, hum)
        print(msg)
        client.publish(mqtt_topic, msg)
    except:
        print("Read or publish error")
    time.sleep(2)
