{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca6fec71",
   "metadata": {
    "vscode": {
     "languageId": "plaintext"
    }
   },
   "outputs": [],
   "source": [
    "#include <Wire.h>\n",
    "#include <Adafruit_MPU6050.h>\n",
    "#include <Adafruit_Sensor.h>\n",
    "#include <DHT.h>\n",
    "\n",
    "#define DHTPIN D4          // GPIO2 on NodeMCU\n",
    "#define DHTTYPE DHT11\n",
    "\n",
    "DHT dht(DHTPIN, DHTTYPE);\n",
    "Adafruit_MPU6050 mpu;\n",
    "\n",
    "void setup() {\n",
    "\n",
    "  Serial.begin(115200);\n",
    "\n",
    "  Wire.begin();\n",
    "\n",
    "  dht.begin();\n",
    "\n",
    "  if (!mpu.begin()) {\n",
    "    Serial.println(\"MPU6050 not found!\");\n",
    "    while (1);\n",
    "  }\n",
    "\n",
    "  Serial.println(\"Satellite Telemetry Started\");\n",
    "}\n",
    "\n",
    "void loop() {\n",
    "\n",
    "  float temperature = dht.readTemperature();\n",
    "  float humidity = dht.readHumidity();\n",
    "\n",
    "  sensors_event_t accel, gyro, temp;\n",
    "\n",
    "  mpu.getEvent(&accel, &gyro, &temp);\n",
    "\n",
    "  Serial.print(\"Temperature:\");\n",
    "  Serial.print(temperature);\n",
    "  Serial.print(\" C\");\n",
    "\n",
    "  Serial.print(\" | Humidity:\");\n",
    "  Serial.print(humidity);\n",
    "  Serial.print(\" %\");\n",
    "\n",
    "  Serial.print(\" | AccX:\");\n",
    "  Serial.print(accel.acceleration.x);\n",
    "\n",
    "  Serial.print(\" | AccY:\");\n",
    "  Serial.print(accel.acceleration.y);\n",
    "\n",
    "  Serial.print(\" | AccZ:\");\n",
    "  Serial.print(accel.acceleration.z);\n",
    "\n",
    "  Serial.print(\" | GyroX:\");\n",
    "  Serial.print(gyro.gyro.x);\n",
    "\n",
    "  Serial.print(\" | GyroY:\");\n",
    "  Serial.print(gyro.gyro.y);\n",
    "\n",
    "  Serial.print(\" | GyroZ:\");\n",
    "  Serial.println(gyro.gyro.z);\n",
    "\n",
    "  delay(2000);\n",
    "}"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
