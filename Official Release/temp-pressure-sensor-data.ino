#include <Wire.h>
#include <Adafruit_BMP280.h>
#include <DallasTemperature.h>
#include <OneWire.h>

#define ONE_WIRE_BUS 4

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
DeviceAddress tempDeviceAddress;

int  resolution = 9;
unsigned long lastTempRequest = 0;
int  delayInMillis = 0;
float temperature = 0.0;
int  idle = 0;
const int len = 5;
double sensorData[len];

Adafruit_BMP280 bmp;
Adafruit_Sensor *bmp_pressure = bmp.getPressureSensor();

void setup(void) {
  Serial.begin(115200);

  if (!bmp.begin(0x76)) {
  }

  bmp.setSampling(Adafruit_BMP280::MODE_NORMAL,     /* Operating Mode. */
                  Adafruit_BMP280::SAMPLING_X2,     /* Temp. oversampling */
                  Adafruit_BMP280::SAMPLING_X16,    /* Pressure oversampling */
                  Adafruit_BMP280::FILTER_X16,      /* Filtering. */
                  Adafruit_BMP280::STANDBY_MS_500); /* Standby time. */

  sensors.begin();
  sensors.getAddress(tempDeviceAddress, 0);
  sensors.setResolution(tempDeviceAddress, resolution);

  sensors.setWaitForConversion(false);
  sensors.requestTemperatures();
  delayInMillis = 750 / (1 << (12 - resolution)); 
  lastTempRequest = millis(); 

  pinMode(13, OUTPUT);
}

void loop(void) {
  if (millis() - lastTempRequest >= delayInMillis) { // waited long enough??
    digitalWrite(13, LOW);
    Serial.println(" Temperature: ");
    for (int i = 0;  i < len;  i++){
      sensorData[i] = sensors.getTempCByIndex(i);
    }

    sensors.requestTemperatures();
    lastTempRequest = millis();
    
    sensors_event_t temp_event, pressure_event;
    bmp_pressure->getEvent(&pressure_event);

    String printString = "";
    for (int i = 0; i < len; i++){
      printString += String(sensorData[i]) + " ";
    }
    Serial.println(printString);
    Serial.print(F("Pressure = "));
    Serial.print((pressure_event.pressure)/10);
    Serial.println(" kPa");

  }
  digitalWrite(13, HIGH);
  delay(1);
}