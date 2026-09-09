import serial, json, time

SERIAL_PORT = "COM3"   # Windows: check Device Manager. Linux: usually /dev/ttyUSB0 or /dev/ttyACM0
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
time.sleep(2)  # allow Arduino to reset after serial connect

def get_telemetry():
    line = ser.readline().decode("utf-8", errors="ignore").strip()
    try:
        data = json.loads(line)
        data["timestamp"] = time.time()
        return data
    except json.JSONDecodeError:
        return None

if __name__ == "__main__":
    while True:
        t = get_telemetry()
        if t:
            print(json.dumps(t, indent=2))