// Project: MainScript
// Author: Christopher Lai
// Contributers: Kevin Brannan, Mohamed Hamida
// Description: Using black-box fused data and filtering for computation.
// Version Control: 2.18.2021
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>


// Default Address for BNO055
Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28);

const int len = 37;
double sensorData[len];
unsigned long last_time = 0, timenow = 0, dt = 0; 

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

  delay(100);
}

// [LOOP] Repeats code in this block
void loop() {
  uint8_t system, gyro, accel, mag;
  bno.getCalibration(&system, &gyro, &accel, &mag);

  //internally blended vectors
  imu::Quaternion quat = bno.getQuat();   //[w,x,y,z]
  imu::Vector<3> orientation = bno.getVector(Adafruit_BNO055::VECTOR_EULER);    //[x,y,z]
  imu::Vector<3> lin_accel = bno.getVector(Adafruit_BNO055::VECTOR_LINEARACCEL);
  imu::Vector<3> grav = bno.getVector(Adafruit_BNO055::VECTOR_GRAVITY);
  timenow = micros();
  dt = timenow - last_time;   //overflow ~70mins.
  last_time = timenow;  //overflow ~70mins.

  
  // Temperature Sensor Readings [5] (on another arduino)

  // IMU Readings [16]
  sensorData[5] = system;   // System Calibration
  sensorData[6] = gyro;     // Gyro Calibration
  sensorData[7] = accel;    // Accel Calibration
  sensorData[8] = mag;      // Magno Calibration
  sensorData[9] = orientation.x();      // Absolute Orientation x-component
  sensorData[10] = orientation.y();     // Absolute Orientation y-component
  sensorData[11] = orientation.z();      // Absolute Orientation z-component
  sensorData[15] = lin_accel.x();     // Linear Acceleration Vector x-component
  sensorData[16] = lin_accel.y();     // Linear Acceleration Vector y-component
  sensorData[17] = lin_accel.z();     // Linear Acceleration Vector z-component
  sensorData[27] = bno.getTemp();     // Ambient Temperature IMU

  
  sensorData[37] = dt; 
  
  for (int i = 0; i < len-1; i++)
  {
    Serial.print(sensorData[i] + " ");
  }
  Serial.println(sensorData[37]); 

  delay(100);
}
