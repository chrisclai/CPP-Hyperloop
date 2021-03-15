// Project: MainScript
// Author: Christopher Lai
// Description: Actual Value Input from other sensors
// Version Control: 2.18.2021

// Include Libraries used to read Dallas Temp Sensors
#include <OneWire.h>
#include <DallasTemperature.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

// Default Address for BNO055
Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28);

const int len = 36;
double sensorData[len];

// [SETUP] Code runs once here
void setup() {
  Serial.begin(115200);
  
  for (int i = 0; i < len; i++)
  {
    sensorData[i] = 0;
  }

  if(!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }

  bno.setExtCrystalUse(true);

  // Serial.println(sensors.getTempCByIndex(0));
  delay(100);
}

// [LOOP] Repeats code in this block
void loop() {
  
  sensors_event_t orientationData , angVelocityData , linearAccelData, magnetometerData, accelerometerData, gravityData;
  bno.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);
  bno.getEvent(&angVelocityData, Adafruit_BNO055::VECTOR_GYROSCOPE);
  bno.getEvent(&linearAccelData, Adafruit_BNO055::VECTOR_LINEARACCEL);
  bno.getEvent(&magnetometerData, Adafruit_BNO055::VECTOR_MAGNETOMETER);
  bno.getEvent(&accelerometerData, Adafruit_BNO055::VECTOR_ACCELEROMETER);
  bno.getEvent(&gravityData, Adafruit_BNO055::VECTOR_GRAVITY);

  uint8_t system, gyro, accel, mag;
  system = gyro = accel = mag = 0;
  bno.getCalibration(&system, &gyro, &accel, &mag);

  // Temperature Sensor Readings [5] (on another arduino)

  // IMU Readings [16]
  sensorData[5] = system;   // System Calibration
  sensorData[6] = gyro;     // Gyro Calibration
  sensorData[7] = accel;    // Accel Calibration
  sensorData[8] = mag;      // Magno Calibration
  sensorData[9] = orientationData.orientation.x;      // Absolute Orientation x-component
  sensorData[10] = orientationData.orientation.y;     // Absolute Orientation y-component
  sensorData[11] = orientationData.orientation.z;      // Absolute Orientation z-component
  sensorData[12] = angVelocityData.gyro.x;      // Angular Velocity Vector x-component
  sensorData[13] = angVelocityData.gyro.y;      // Angular Velocity Vector y-component
  sensorData[14] = angVelocityData.gyro.z;     // Angular Velocity Vector z-component
  sensorData[15] = linearAccelData.acceleration.x;     // Linear Acceleration Vector x-component
  sensorData[16] = linearAccelData.acceleration.y;     // Linear Acceleration Vector y-component
  sensorData[17] = linearAccelData.acceleration.z;     // Linear Acceleration Vector z-component
  sensorData[18] = magnetometerData.magnetic.x;     // Magnometer Vector x-component
  sensorData[19] = magnetometerData.magnetic.y;     // Magnometer Vector y-component
  sensorData[20] = magnetometerData.magnetic.z;     // Magnometer Acceleration Vector z-component
  sensorData[21] = gravityData.acceleration.x;     // Gravit. Acceleration Vector x-component
  sensorData[22] = gravityData.acceleration.y;     // Gravit. Acceleration y-component
  sensorData[23] = gravityData.acceleration.z;     // Gravit. Acceleration z-component
  sensorData[24] = accelerometerData.acceleration.x;     // Total Acceleration Vector x-component
  sensorData[25] = accelerometerData.acceleration.y;     // Total Acceleration Vector y-component
  sensorData[26] = accelerometerData.acceleration.z;     // Total Acceleration Vector z-component
  sensorData[27] = bno.getTemp();     // Ambient Temperature IMU

  // Pressure Sensor [1]
  sensorData[28] = 0; // Pressure in kPa

  // Current + Voltage Sensor [5]
  sensorData[29] = 0;   // Motor Voltage (V)
  sensorData[30] = 0;  // Motor Current (mA)
  sensorData[31] = 0;   // Battery Voltage (V)
  sensorData[32] = 0;  // Battery Current (mA)
  sensorData[33] = 0;  // Battery Capacity (%)

  // Output Status [2]

  String printString = "";
  for (int i = 0; i < len; i++)
  {
    printString += String(sensorData[i]) + " ";
  }
  Serial.println(printString);

  delay(100);
}
