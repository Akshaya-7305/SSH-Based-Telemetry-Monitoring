#include <Wire.h>
#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

// MPU6050 I2C Address
const byte MPU = 0x68;

void setup() {
  Serial.begin(9600);
  Wire.begin();

  // Wake up MPU6050
  Wire.beginTransmission(MPU);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);

  dht.begin();

  Serial.println("Satellite Telemetry Started");
}

void loop() {

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  // Read accelerometer and gyroscope
  Wire.beginTransmission(MPU);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU, (uint8_t)14);

  int16_t AcX = Wire.read() << 8 | Wire.read();
  int16_t AcY = Wire.read() << 8 | Wire.read();
  int16_t AcZ = Wire.read() << 8 | Wire.read();

  // Skip temperature bytes
  Wire.read();
  Wire.read();

  int16_t GyX = Wire.read() << 8 | Wire.read();
  int16_t GyY = Wire.read() << 8 | Wire.read();
  int16_t GyZ = Wire.read() << 8 | Wire.read();

  Serial.print("TEMP:");
  Serial.print(temperature);

  Serial.print(", HUM:");
  Serial.print(humidity);

  Serial.print(", ACCX:");
  Serial.print(AcX);

  Serial.print(", ACCY:");
  Serial.print(AcY);

  Serial.print(", ACCZ:");
  Serial.print(AcZ);

  Serial.print(", GYRX:");
  Serial.print(GyX);

  Serial.print(", GYRY:");
  Serial.print(GyY);

  Serial.print(", GYRZ:");
  Serial.println(GyZ);

  delay(2000);
}
