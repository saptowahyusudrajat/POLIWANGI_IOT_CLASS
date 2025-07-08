import dht
import machine
import time
import network

sensor = dht.DHT11(machine.Pin(4))

# WiFi credentials
WIFI_SSID = "Pixel"
WIFI_PASSWORD = "saptoganteng"

def connect_wifi():
    # Create station interface
    sta_if = network.WLAN(network.STA_IF)
    
    # Activate the interface
    if not sta_if.isconnected():
        print("Connecting to WiFi...")
        sta_if.active(True)
        sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
        
        # Wait for connection
        while not sta_if.isconnected():
            print(".", end="")
            time.sleep(0.5)
    
    # Print connection details
    print("\nConnected!")
    print("Network config:", sta_if.ifconfig())

# Connect to WiFi
connect_wifi()

while True:
    sensor.measure()
    print("Temp: ", sensor.temperature(), "degC")
    print("Hum: ", sensor.humidity(), "%")
    time.sleep(1)
    