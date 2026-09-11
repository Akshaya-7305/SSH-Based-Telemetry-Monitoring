import serial
import time

# Arduino is connected to COM8
arduino = serial.Serial("COM8", 9600, timeout=1)

# Give Arduino a moment after opening the serial connection
time.sleep(2)

print("Connected to Arduino on COM8")
print("Waiting for data...\n")

while True:
    data = arduino.readline().decode("utf-8", errors="ignore").strip()

    if data:
        print("Received:", data)