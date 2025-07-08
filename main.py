import dht
import machine
import time
import network

d = dht.DHT11(machine.Pin(4))

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect('InixindoZone', 'inix2023surabaya')
        
        while not wlan.isconnected():
            time.sleep(1)
           
    if wlan.isconnected():
        print("Connected. IP:", wlan.ifconfig()[0])
    else:
        print("WiFi connection failed.")

connect_wifi()

while True:
    
    d.measure()
    print("Temp: ", d.temperature(), "degC")
    print("Hum: ", d.humidity(), "%")
    time.sleep(1)
    