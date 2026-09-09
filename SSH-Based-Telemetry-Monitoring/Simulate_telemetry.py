import random
import time

def get_telemetry():
    return {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "temperature_C": round(random.uniform(20, 35), 2),
        "humidity_percent": round(random.uniform(40, 70), 2),
        "accel_xyz": [
            round(random.uniform(-1, 1), 2),
            round(random.uniform(-1, 1), 2),
            round(random.uniform(-1, 1), 2)
        ],
        "gyro_xyz": [
            round(random.uniform(-5, 5), 2),
            round(random.uniform(-5, 5), 2),
            round(random.uniform(-5, 5), 2)
        ]
    }


if __name__ == "__main__":
    while True:
        print(get_telemetry())
        time.sleep(2)