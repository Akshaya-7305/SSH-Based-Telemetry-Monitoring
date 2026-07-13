import time
import random

try:
    import board
    import busio
    import adafruit_dht
    import adafruit_mpu6050

    # Initialize sensors
    dht = adafruit_dht.DHT11(board.D4)

    i2c = busio.I2C(board.SCL, board.SDA)
    mpu = adafruit_mpu6050.MPU6050(i2c)

    SENSOR_AVAILABLE = True

except ImportError:
    print("Real sensors not available. Using simulated telemetry.")
    SENSOR_AVAILABLE = False


def get_telemetry():
    if SENSOR_AVAILABLE:
        try:
            temperature = dht.temperature
            humidity = dht.humidity

            accel = mpu.acceleration
            gyro = mpu.gyro

            return {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "temperature_C": temperature,
                "humidity_percent": humidity,
                "accel_xyz": [
                    round(accel[0], 2),
                    round(accel[1], 2),
                    round(accel[2], 2)
                ],
                "gyro_xyz": [
                    round(gyro[0], 2),
                    round(gyro[1], 2),
                    round(gyro[2], 2)
                ]
            }

        except RuntimeError:
            # Sensor read failed, fall back to simulation
            pass

    # Simulated telemetry
    return {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "temperature_C": round(random.uniform(20.0, 35.0), 2),
        "humidity_percent": round(random.uniform(40.0, 70.0), 2),
        "accel_xyz": [
            round(random.uniform(-2.0, 2.0), 2),
            round(random.uniform(-2.0, 2.0), 2),
            round(random.uniform(8.0, 10.0), 2)
        ],
        "gyro_xyz": [
            round(random.uniform(-250.0, 250.0), 2),
            round(random.uniform(-250.0, 250.0), 2),
            round(random.uniform(-250.0, 250.0), 2)
        ]
    }


if __name__ == "__main__":
    while True:
        print(get_telemetry())
        time.sleep(2)
