import time
import board
import busio
import adafruit_dht
import adafruit_mpu6050

dht = adafruit_dht.DHT11(board.D4)

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)


def get_telemetry():
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