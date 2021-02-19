// Project: MainScript
// Author: Christopher Lai
// Description: Actual Value Input from other sensors
// Version Control: 2.18.2021

#include <OneWire.h>
#include <DallasTemperature.h>

#define tempSensor 2
#define DCMotor 7
#define brakeLED1 8
#define brakeLED2 9

int deviceCount = 0;

OneWire oneWire (tempSensor);

DallasTemperature sensors(&oneWire);

void RPiSerial()  // Checks to see if serial data has been recieved from the Raspberry Pi
{
  if (Serial.available())
  {
    String command = Serial.readString();
    if (command == "brake")
    {
      digitalWrite(brakeLED1, HIGH);
      digitalWrite(brakeLED2, HIGH);
    }
    else if (command == "unbrake")
    {
      digitalWrite(brakeLED1, LOW);
      digitalWrite(brakeLED2, LOW);
    }
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(brakeLED1, OUTPUT);
  digitalWrite(brakeLED1, LOW);

  pinMode(brakeLED2, OUTPUT);
  digitalWrite(brakeLED2, LOW);

  randomSeed(analogRead(0));  // Generate Random Numbers
  
  sensors.begin();

  // locate devices on the bus
  Serial.print("Locating devices...");
  Serial.print("Found ");
  deviceCount = sensors.getDeviceCount();
  Serial.print(deviceCount, DEC);
  Serial.println(" devices.");
  Serial.println("");
}

void loop() {
  // put your main code here, to run repeatedly:

  // Unused code for this example, normally would be for temperature data
  sensors.requestTemperatures();

  double sensorData[27];
  
  // Temperature Sensor Readings [5]
  for (int i = 0;  i < deviceCount;  i++)
  {
    sensorData[i] = sensors.getTempCByIndex(i);
  }

  // IMU Readings [16]
  sensorData[5] = random(100);      // Absolute Orientation x-component
  sensorData[6] = random(100);      // Absolute Orientation y-component
  sensorData[7] = random(100);      // Absolute Orientation z-component
  sensorData[8] = random(100);      // Angular Velocity Vector x-component
  sensorData[9] = random(100);      // Angular Velocity Vector y-component
  sensorData[10] = random(100);     // Angular Velocity Vector z-component
  sensorData[11] = random(100);     // Acceleration Vector x-component
  sensorData[12] = random(100);     // Acceleration Vector y-component
  sensorData[13] = random(100);     // Acceleration Vector z-component
  sensorData[14] = random(100);     // Linear Acceleration Vector x-component
  sensorData[15] = random(100);     // Linear Acceleration Vector y-component
  sensorData[16] = random(100);     // Linear Acceleration Vector z-component
  sensorData[17] = random(100);     // Gravity Vector x-component
  sensorData[18] = random(100);     // Gravity Vector y-component
  sensorData[19] = random(100);     // Gravity Vector z-component
  sensorData[20] = random(20, 40);  // Ambient Temperature IMU

  // Pressure Sensor [1]
  sensorData[21] = random(50, 150); // Pressure in kPa

  // Current + Voltage Sensor [5]
  sensorData[22] = random(30, 70);   // Motor Voltage (V)
  sensorData[23] = random(50, 100);  // Motor Current (mA)
  sensorData[24] = random(30, 70);   // Battery Voltage (V)
  sensorData[25] = random(50, 100);  // Battery Current (mA)
  sensorData[26] = random(90, 100);  // Battery Capacity (%)

  String printString = "";
  for (int i = 0; i < 27; i++)
  {
    printString += String(sensorData[i]) + " ";
  }
  Serial.println(printString);
  
  RPiSerial();

  delay(100);
}
