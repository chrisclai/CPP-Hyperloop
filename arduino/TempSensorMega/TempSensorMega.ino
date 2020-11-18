// Project: Temperature Sensor Using DS18B20 for CPP Hyperloop 2020
// Author: Christopher Lai
// Version Control: 11.18.2020

#include <OneWire.h>
#include <DallasTemperature.h>

#define tempSensor 6

OneWire oneWire (tempSensor);

DallasTemperature sensors(&oneWire);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  sensors.begin();
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:
  sensors.requestTemperatures();
  double tempF = sensors.getTempFByIndex(0);
  Serial.println(String(tempF) + "F");
  delay(100);
}
