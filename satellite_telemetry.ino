#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>

#define DHTPIN D4          // GPIO2 on NodeMCU
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);
Adafruit_MPU6050 mpu;

void setup() {

  Serial.begin(115200);

  Wire.begin();

  dht.begin();

  if (!mpu.begin()) {
    Serial.println("MPU6050 not found!");
    while (1);
  }

  Serial.println("Satellite Telemetry Started");
}

void loop() {

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  sensors_event_t accel, gyro, temp;

  mpu.getEvent(&accel, &gyro, &temp);

  Serial.print("Temperature:");
  Serial.print(temperature);
  Serial.print(" C");

  Serial.print(" | Humidity:");
  Serial.print(humidity);
  Serial.print(" %");

  Serial.print(" | AccX:");
  Serial.print(accel.acceleration.x);

  Serial.print(" | AccY:");
  Serial.print(accel.acceleration.y);

  Serial.print(" | AccZ:");
  Serial.print(accel.acceleration.z);

  Serial.print(" | GyroX:");
  Serial.print(gyro.gyro.x);

  Serial.print(" | GyroY:");
  Serial.print(gyro.gyro.y);

  Serial.print(" | GyroZ:");
  Serial.println(gyro.gyro.z);

  delay(2000);
}
