// Project: DataTest
// Author: Christopher Lai
// Description: Prints out random numbers signifying each sensor to the serial monitor.
// Please refer to the CPP Hyperloop spreadsheet for specific array IDs.
// Version Control: 2.7.2021

#define tempSensor 6
#define testLED 13

void RPiSerial()  // Checks to see if serial data has been recieved from the Raspberry Pi
{
  if (Serial.available())
  {
    String command = Serial.readString();
    if (command == "start")
    {
      digitalWrite(testLED, HIGH);
    }
    else if (command == "stop")
    {
      digitalWrite(testLED, LOW);
    }
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(testLED, OUTPUT);   // Use the on-board LED on the Arduino to test input from GUI
  digitalWrite(testLED, LOW); // On-start, LED is OFF by default

  randomSeed(analogRead(0));  // Generate Random Numbers
  
  // sensors.begin();
  // delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:

  // Unused code for this example, normally would be for temperature data
  // sensors.requestTemperatures();
  // double tempF = sensors.getTempFByIndex(0);
  // Serial.println(String(tempF) + "F");

  int sensorData[30];

  // Temperature Sensor Readings [5]
  sensorData[0] = random(20, 40); // Temp Sensor Motor Controller 1
  sensorData[1] = random(20, 40); // Temp Sensor Motor Controller 2
  sensorData[2] = random(20, 40); // Temp Sensor Motor 1
  sensorData[3] = random(20, 40); // Temp Sensor Motor 2
  sensorData[4] = random(20, 40); // Temp Sensor Battery System

  // IMU Readings [16]
  sensorData[5] = random(100);      // Absolute Orientation x-component
  sensorData[6] = random(100);      // Absolute Orientation y-component
  sensorData[7] = random(100);      // Absolute Orientation z-component
  sensorData[8] = random(100);      // Angular Velocity Vector x-component
  sensorData[9] = random(100);      // Absolute Orientation x-component
  sensorData[10] = random(100);      // Absolute Orientation y-component
  sensorData[11] = random(100);      // Absolute Orientation z-component
  sensorData[12] = random(100);      // Angular Velocity Vector x-component
  sensorData[13] = random(100);      // Angular Velocity Vector y-component
  sensorData[14] = random(100);     // Angular Velocity Vector z-component
  sensorData[15] = random(100);     // Acceleration Vector x-component
  sensorData[16] = random(100);     // Acceleration Vector y-component
  sensorData[17] = random(100);     // Acceleration Vector z-component
  sensorData[18] = random(100);     // Linear Acceleration Vector x-component
  sensorData[19] = random(100);     // Linear Acceleration Vector y-component
  sensorData[20] = random(100);     // Linear Acceleration Vector z-component
  sensorData[21] = random(100);     // Gravity Vector x-component
  sensorData[22] = random(100);     // Gravity Vector y-component
  sensorData[23] = random(100);     // Gravity Vector z-component
  sensorData[24] = random(20, 40);  // Ambient Temperature IMU

  // Pressure Sensor [1]
  sensorData[25] = random(50, 150); // Pressure in kPa

  // Current + Voltage Sensor [5]
  sensorData[26] = random(30, 70);   // Motor Voltage (V)
  sensorData[27] = random(50, 100);  // Motor Current (mA)
  sensorData[28] = random(30, 70);   // Battery Voltage (V)
  sensorData[29] = random(50, 100);  // Battery Current (mA)
  sensorData[30] = random(90, 100);  // Battery Capacity (%)

  String printString = "";
  for (int i = 0; i < 30; i++)
  {
    printString += String(sensorData[i]) + " ";
  }
  Serial.println(printString);
  
  RPiSerial();

  delay(100);
}
