// Project: Temperature Sensor for CPP Hyperloop 2020
// Author: Christopher Lai
// Version Control: 9.24.20 4:26:19PM


// Make sure you have these three libraries downloaded!
#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include <DHT.h>

LiquidCrystal_I2C lcd(0x27,16,2);

#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

const int button = 6;

const int blueLED = 8;
const int greenLED = 9;
const int redLED = 10;

int logic = HIGH;
int currentState;
int previousState = LOW;

long timeInit = 0;
long debounce = 200;

float h;
float t;
float f;

void setup() {
  Serial.begin(9600);

  // Setup LCDs  
  lcd.init();
  lcd.backlight();

  // Setup DHT11 Sensor
  Serial.println(F("DHT test"));
  dht.begin();

  // Setup I/O Pins
  pinMode(button, INPUT);

  pinMode(blueLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);
}

void loop() {
  delay(1000);    // Short delay to allow the sensor to detect data more accurately

  buttonCheck(); // Check if the button is pressed or not                         
   
  h = dht.readHumidity();        // Read Humidity
  t = dht.readTemperature();     // Temperature in Celsius
  f = dht.readTemperature(true); // Temperature in Fahrenheit

  // Check if any of the readings fails and has a null value
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  tempCheck();   // Check to see what temperature it is, and light up the LEDs accordingly

  // Prints results to LCD Display. Button presses will toggle display between
  // Fahrenheit and Celsius values
  lcd.setCursor(0,0);
  lcd.print("Humidity: " + String(h) + "%");
  if (logic)
  {
    lcd.setCursor(0,1);
    lcd.print("Temp:     " + String(t) + "C");
  }
  else
  {
    lcd.setCursor(0,1);
    lcd.print("Temp:     " + String(f) + "F");
  }
}

// Check to see if a button has been pressed
void buttonCheck()
{
  currentState = digitalRead(button);
  if (currentState == HIGH && previousState == LOW && millis() - timeInit > debounce) {
    if (logic == HIGH)
      logic = LOW;
    else
      logic = HIGH;

    timeInit = millis();    
  }
  previousState = currentState;
}

// Light up the LEDs appropriately with the specified temperature
void tempCheck()
{
  digitalWrite(blueLED, LOW);
  digitalWrite(greenLED, LOW);
  digitalWrite(redLED, LOW);

  if (f > 80)
  {
    digitalWrite(redLED, HIGH);
  }
  else if (f < 75)
  {
    digitalWrite(blueLED, HIGH);
  }
  else
  {
    digitalWrite(greenLED, HIGH);
  }
}
