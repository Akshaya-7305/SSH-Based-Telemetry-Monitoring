import smbus
import time
import Adafruit_DHT
import socket
import json

# ---------------- DHT11 ---------------- #
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

# ---------------- MPU6050 ---------------- #
bus = smbus.SMBus(1)
MPU_ADDR = 0x68

# Wake up MPU6050
bus.write_byte_data(MPU_ADDR, 0x6B, 0)

def read_raw_data(addr):
    high = bus.read_byte_data(MPU_ADDR, addr)
    low = bus.read_byte_data(MPU_ADDR, addr + 1)

    value = (high << 8) | low

    if value > 32768:
        value -= 65536

    return value

# ---------------- Socket ---------------- #
PC1_IP = "192.168.1.100"
PC2_IP = "192.168.1.101"

PORT = 5000

pc1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pc2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    pc1.connect((PC1_IP, PORT))
except:
    print("PC1 Not Connected")

try:
    pc2.connect((PC2_IP, PORT))
except:
    print("PC2 Not Connected")

print("Satellite Telemetry Started")

while True:

    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    ax = read_raw_data(0x3B) / 16384.0
    ay = read_raw_data(0x3D) / 16384.0
    az = read_raw_data(0x3F) / 16384.0

    gx = read_raw_data(0x43) / 131.0
    gy = read_raw_data(0x45) / 131.0
    gz = read_raw_data(0x47) / 131.0

    telemetry = {
        "Temperature": round(temperature, 2) if temperature else None,
        "Humidity": round(humidity, 2) if humidity else None,
        "Accel_X": round(ax, 2),
        "Accel_Y": round(ay, 2),
        "Accel_Z": round(az, 2),
        "Gyro_X": round(gx, 2),
        "Gyro_Y": round(gy, 2),
        "Gyro_Z": round(gz, 2),
        "Timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    data = json.dumps(telemetry)

    print(data)

    try:
        pc1.send((data + "\n").encode())
    except:
        pass

    try:
        pc2.send((data + "\n").encode())
    except:
        pass

    time.sleep(2)