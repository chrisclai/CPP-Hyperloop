// Project: MainScript
// Author: Christopher Lai
/* Contributers: Kevin Brannan, Mohamed Hamida */
// Description: Using black-box fused data and filtering for computation.
// Version Control: 2.18.2021
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>

//#include <utility/imumaths.h>

// Default Address for BNO055
Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28);

const int len = 37;
double sensorData[len];
unsigned long last_time = 0, timenow = 0, dt = 0; 

//sensors_event_t orientationData , angVelocityData , linearAccelData, magnetometerData, accelerometerData, gravityData;

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
  uint8_t system, gyro, accel, mag;
  bno.getCalibration(&system, &gyro, &accel, &mag);
  //bno.isFullyCalibrated();   //bool

/*
  bno.getEvent(&orientationData, Adafruit_BNO055::VECTOR_EULER);
  bno.getEvent(&angVelocityData, Adafruit_BNO055::VECTOR_GYROSCOPE);
  bno.getEvent(&linearAccelData, Adafruit_BNO055::VECTOR_LINEARACCEL);
  bno.getEvent(&magnetometerData, Adafruit_BNO055::VECTOR_MAGNETOMETER);
  bno.getEvent(&accelerometerData, Adafruit_BNO055::VECTOR_ACCELEROMETER);
  bno.getEvent(&gravityData, Adafruit_BNO055::VECTOR_GRAVITY);
*/

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
  //sensorData[12] = angVelocityData.gyro.x;      // Angular Velocity Vector x-component
  //sensorData[13] = angVelocityData.gyro.y;      // Angular Velocity Vector y-component
  //sensorData[14] = angVelocityData.gyro.z;     // Angular Velocity Vector z-component
  sensorData[15] = lin_accel.x();     // Linear Acceleration Vector x-component
  sensorData[16] = lin_accel.y();     // Linear Acceleration Vector y-component
  sensorData[17] = lin_accel.z();     // Linear Acceleration Vector z-component
  //sensorData[18] = magnetometerData.magnetic.x;     // Magnometer Vector x-component
  //sensorData[19] = magnetometerData.magnetic.y;     // Magnometer Vector y-component
  //sensorData[20] = magnetometerData.magnetic.z;     // Magnometer Acceleration Vector z-component
  //sensorData[21] = gravityData.acceleration.x;     // Gravit. Acceleration Vector x-component
  //sensorData[22] = gravityData.acceleration.y;     // Gravit. Acceleration y-component
  //sensorData[23] = gravityData.acceleration.z;     // Gravit. Acceleration z-component
  //sensorData[24] = accelerometerData.acceleration.x;     // Total Acceleration Vector x-component
  //sensorData[25] = accelerometerData.acceleration.y;     // Total Acceleration Vector y-component
  //sensorData[26] = accelerometerData.acceleration.z;     // Total Acceleration Vector z-component
  sensorData[27] = bno.getTemp();     // Ambient Temperature IMU

  // Pressure Sensor [1]
  //sensorData[28] = 0; // Pressure in kPa

  // Current + Voltage Sensor [5]
  //sensorData[29] = 0;   // Motor Voltage (V)
  //sensorData[30] = 0;  // Motor Current (mA)
  //sensorData[31] = 0;   // Battery Voltage (V)
  //sensorData[32] = 0;  // Battery Current (mA)
  //sensorData[33] = 0;  // Battery Capacity (%)
  
  sensorData[37] = dt; 
  // Output Status [2]
  String printString = "";

  for (int i = 0; i < len-1; i++)
  {
    printString += String(sensorData[i]) + " ";
  }
  
  Serial.print(printString);
  Serial.println(sensorData[37]); 

  delay(100);
}
