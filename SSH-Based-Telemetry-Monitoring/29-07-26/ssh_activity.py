import serial
import time

PORT = "/dev/ttyUSB0"
BAUD = 9600

try:
    arduino = serial.Serial(PORT, BAUD, timeout=1)

    # Nano may reset when serial connection opens
    time.sleep(2)

    arduino.write(b"ACTIVITY\n")
    arduino.flush()

    time.sleep(0.4)

    arduino.close()

except Exception:
    pass