import serial
import time

arduino = serial.Serial("COM8", 9600, timeout=1)

time.sleep(2)

print("Connected to Arduino on COM8")
print("Waiting for data...\n")

while True:
    data = arduino.readline().decode("utf-8", errors="ignore").strip()

    if data:
        print("Received:", data)