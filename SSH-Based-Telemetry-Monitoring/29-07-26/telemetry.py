import random
import time
from datetime import datetime


def generate_telemetry():

    temperature = round(random.uniform(20, 35), 2)
    humidity = round(random.uniform(40, 70), 2)

    accel_x = round(random.uniform(-1, 1), 2)
    accel_y = round(random.uniform(-1, 1), 2)
    accel_z = round(random.uniform(9.5, 10.0), 2)

    battery = round(random.uniform(70, 100), 2)
    voltage = round(random.uniform(3.7, 4.2), 2)

    if temperature > 32:
        status = "WARNING"
    else:
        status = "NORMAL"

    return {
        "temperature": temperature,
        "humidity": humidity,
        "accel_x": accel_x,
        "accel_y": accel_y,
        "accel_z": accel_z,
        "battery": battery,
        "voltage": voltage,
        "status": status
    }


def display_telemetry(data):

    print("\n====================================")
    print("      SATELLITE TELEMETRY")
    print("====================================")

    print("Time        :", datetime.now().strftime("%H:%M:%S"))
    print("Temperature :", data["temperature"], "C")
    print("Humidity    :", data["humidity"], "%")

    print("Accel X     :", data["accel_x"])
    print("Accel Y     :", data["accel_y"])
    print("Accel Z     :", data["accel_z"])

    print("Battery     :", data["battery"], "%")
    print("Voltage     :", data["voltage"], "V")

    print("Status      :", data["status"])

    print("====================================")


print("REMOTE SATELLITE TELEMETRY STARTED")
print("Press Ctrl+C to stop")

try:

    while True:

        telemetry = generate_telemetry()

        display_telemetry(telemetry)

        time.sleep(5)

except KeyboardInterrupt:

    print("\nTelemetry monitoring stopped.")