//
// Sample of using Async reading of Dallas Temperature Sensors
// 
#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into port 2 on the Arduino
#define ONE_WIRE_BUS 2

// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors(&oneWire);

DeviceAddress tempDeviceAddress;

int  resolution = 9;
unsigned long lastTempRequest = 0;
int  delayInMillis = 0;
float temperature = 0.0;
int  idle = 0;

const int len = 6;
double sensorData[len];

//
// SETUP
//
void setup(void)
{
  Serial.begin(115200);
  // Serial.println("Dallas Temperature Control Library - Async Demo");
  // Serial.print("Library Version: ");
  // Serial.println(DALLASTEMPLIBVERSION);
  // Serial.println("\n");

  sensorData[0] = -1;

  sensors.begin();
  sensors.getAddress(tempDeviceAddress, 0);
  sensors.setResolution(tempDeviceAddress, resolution);
  
  sensors.setWaitForConversion(false);
  sensors.requestTemperatures();
  delayInMillis = 750 / (1 << (12 - resolution)); 
  lastTempRequest = millis(); 
  
  pinMode(13, OUTPUT); 
}

void loop(void)
{ 
  
  if (millis() - lastTempRequest >= delayInMillis) // waited long enough??
  {
    digitalWrite(13, LOW);
    // Serial.println(" Temperature: ");
    for (int i = 1;  i < len;  i++)
    {
      sensorData[i] = sensors.getTempCByIndex(i - 1);     
    } 
    // Serial.print("  Resolution: ");
    // Serial.println(resolution); 
    // Serial.print("Idle counter: ");
    // Serial.println(idle);     
    
    sensors.requestTemperatures();
    lastTempRequest = millis();

    String printString = "";
    for (int i = 0; i < len; i++)
    {
      printString += String(sensorData[i]) + " ";
    }
    Serial.println(printString);
  }
  digitalWrite(13, HIGH);  
  delay(1);
}
