// Project: Temperature Sensor Using DS18B20 for CPP Hyperloop 2020
// Author: Christopher Lai
// Version Control: 10.1.2020 3:17:59AM

#include <OneWire.h>
#include <DallasTemperature.h>
#include <LiquidCrystal_I2C.h>
#include <Wire.h>

#define tempSensor 2

OneWire oneWire(tempSensor);

DallasTemperature sensors(&oneWire);

LiquidCrystal_I2C lcd(0x27,16,2);

const int whiteLED = 8;
const int blueLED = 9;
const int greenLED = 10;
const int redLED = 11;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  lcd.init();
  lcd.backlight();

  pinMode(whiteLED, OUTPUT);
  pinMode(blueLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);

  digitalWrite(whiteLED, LOW);
  
  sensors.begin();
  delay(1000);
}

void loop() {
  
  // Retrieve sensor temperature values
  sensors.requestTemperatures();
  double tempF = sensors.getTempFByIndex(0);
  double tempC = sensors.getTempCByIndex(0);

  // Display values on the LCD Display
  lcd.setCursor(0,0);
  lcd.print("TempF:    " + String(tempF) + "F");
  lcd.setCursor(0,1);
  lcd.print("TempC:    " + String(tempC) + "C");
  
  Serial.println(tempF); 

  int red = 0;
  int green = 0;
  int blue = 0;

  // Map the temperature detected to the color pertaining to that temperature
  if (tempF > 80)
  {
    red = map(tempF, 80, 85, 127, 255);
    green = map(tempF, 80, 85, 32, 0); 
  }
  else if (tempF > 75)
  {
    red = map(tempF, 75, 80, 0, 127);
    green = map(tempF, 75, 80, 255, 32);
  }
  else
  {
    green = map(tempF, 70, 75, 0, 127);
    blue = map(tempF, 70, 75, 255, 0);
  }

  RGB_color(red,green,blue);
  RPiSerial();
  
  delay(50);
}

// Tell the LED to display a certain color
void RGB_color(int red, int green, int blue)
{
  analogWrite(redLED, red);
  analogWrite(greenLED, green);
  analogWrite(blueLED, blue);
}

void RPiSerial()
{
  if (Serial.available())
  {
    String command = Serial.readString();
    if (command == "led_on")
    {
      digitalWrite(whiteLED, HIGH);
    }
    else if (command == "led_off")
    {
      digitalWrite(whiteLED, LOW);
    }
  }
}
