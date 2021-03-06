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

// Define Pin Values
#define tempSensor 2
#define DCMotor 7
#define brakeLED1 8
#define brakeLED2 9

// Default Address for BNO055
Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28);

// Global Variables
int deviceCount = 0;
int resolution = 12;
unsigned long lastTempRequest = 0;
int delayInMillis = 0;
float temperature = 0.0;
int idle = 0;

const int len = 32;
double sensorData[len];

// OneWire communication port (will find any oneWire device)
OneWire oneWire (tempSensor);

// Create a DTemp object by passing in oneWire object
DallasTemperature sensors(&oneWire);

// [Function] Checks to see if serial data has been recieved from the Raspberry Pi
String RPiSerial()
{
  if (Serial.available())
  {
    String command = Serial.readString();
    // Currently, if string recieved == "brakeon", turn LED on, vice versa for off
    if (command == "brakeon")
    {
      digitalWrite(brakeLED1, HIGH);
      digitalWrite(brakeLED2, HIGH);
      return "brakeon";
    }
    else if (command == "brakeoff")
    {
      digitalWrite(brakeLED1, LOW);
      digitalWrite(brakeLED2, LOW);
      return "brakeon";
    }
    else if (command == "motoron")
    {
      digitalWrite(DCMotor, HIGH);
      return "motoron";
    }
    else if (command == "motoroff")
    {
      digitalWrite(DCMotor, LOW);
      return "motoroff";
    }
    return "nothing";
  }
}

// [SETUP] Code runs once here
void setup() {
  Serial.begin(115200);

  pinMode(brakeLED1, OUTPUT);
  digitalWrite(brakeLED1, LOW);

  pinMode(brakeLED2, OUTPUT);
  digitalWrite(brakeLED2, LOW);

  pinMode(DCMotor, OUTPUT);
  digitalWrite(DCMotor, LOW);
  
  sensors.begin();

  sensors.setWaitForConversion(false);
  sensors.requestTemperatures();
  delayInMillis = 750 / (1 << (12 - resolution));
  lastTempRequest = millis();

  // locate devices on the bus
  // Serial.print("Locating devices...");
  // Serial.print("Found ");
  // deviceCount = sensors.getDeviceCount();
  // Serial.print(deviceCount, DEC);
  // Serial.println(" devices.");
  // Serial.println("");

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
  delay(1000);
}

// [LOOP] Repeats code in this block
void loop() {
  
  sensors_event_t event;
  bno.getEvent(&event);

  uint8_t system, gyro, accel, mag;
  system = gyro = accel = mag = 0;
  bno.getCalibration(&system, &gyro, &accel, &mag);

  // Temperature Sensor Readings [5]
  if (millis() - lastTempRequest >= delayInMillis)
  {
    for (int i = 0;  i < 5;  i++)
    {
      sensorData[i] = sensors.getTempCByIndex(i);      
    }
    lastTempRequest = millis();
    sensors.requestTemperatures();
  }

  // IMU Readings [16]
  sensorData[5] = system;   // System Calibration
  sensorData[6] = gyro;     // Gyro Calibration
  sensorData[7] = accel;    // Accel Calibration
  sensorData[8] = mag;      // Magno Calibration
  sensorData[9] = event.orientation.x;      // Absolute Orientation x-component
  sensorData[10] = event.orientation.y;     // Absolute Orientation y-component
  sensorData[11] = event.orientation.z;      // Absolute Orientation z-component
  sensorData[12] = 0;      // Angular Velocity Vector x-component
  sensorData[13] = 0;      // Angular Velocity Vector y-component
  sensorData[14] = 0;     // Angular Velocity Vector z-component
  sensorData[15] = 0;     // Acceleration Vector x-component
  sensorData[16] = 0;     // Acceleration Vector y-component
  sensorData[17] = 0;     // Acceleration Vector z-component
  sensorData[18] = 0;     // Linear Acceleration Vector x-component
  sensorData[19] = 0;     // Linear Acceleration Vector y-component
  sensorData[20] = 0;     // Linear Acceleration Vector z-component
  sensorData[21] = 0;     // Gravity Vector x-component
  sensorData[22] = 0;     // Gravity Vector y-component
  sensorData[23] = 0;     // Gravity Vector z-component
  sensorData[24] = 0;     // Ambient Temperature IMU

  // Pressure Sensor [1]
  sensorData[25] = 0; // Pressure in kPa

  // Current + Voltage Sensor [5]
  sensorData[26] = 0;   // Motor Voltage (V)
  sensorData[27] = 0;  // Motor Current (mA)
  sensorData[28] = 0;   // Battery Voltage (V)
  sensorData[29] = 0;  // Battery Current (mA)
  sensorData[30] = 0;  // Battery Capacity (%)

  // Output Status [2]
  String inputStat = RPiSerial();
  if (inputStat != "nothing")
  {
    if (inputStat == "brakeon")
    {
      sensorData[31] = 1;
    }
    else if (inputStat == "brakeoff")
    {
      sensorData[31] = 0;
    }
    else if (inputStat == "motoron")
    {
      sensorData[32] = 1;
    }
    else if (inputStat == "motoroff")
    {
      sensorData[32] = 0;
    }
  }

  String printString = "";
  for (int i = 0; i < len; i++)
  {
    printString += String(sensorData[i]) + " ";
  }
  Serial.println(printString);

  delay(50);
}
