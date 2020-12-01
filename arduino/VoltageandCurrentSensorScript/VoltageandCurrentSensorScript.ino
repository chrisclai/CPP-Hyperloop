/*
Measuring Current Using ACS712 and Voltage from Voltage Sensor from MH Electronic
*/

const int analogInVoltage = A1; //Raw Voltage Sensor Input
const int analogInCurrent = A0; //Raw Current Sensor Input
int mVperAmp = 66; // 66 for 30A Module *From Current Sensor Datasheet
int RawValue= 0; //set variable for current sensor raw values
int ACSoffset = 2500; //AC offset for voltage sensor
double Vdc = 0; //voltage variable from current sensor
double Amps = 0; //variable for current sensor
double volts = 0; //raw value from voltage sensor
int offset = 20; //offset for voltage sensor correction *if needed

void setup(){
Serial.begin(9600);
}

void loop(){
  
  //Voltage Sensor
  volts = analogRead(analogInVoltage); // read input
  double voltage = map(volts, 0, 1023, 0, 2500); //map 0-1023 to 0-2500 and add correction offset if needed
  voltage /=100; //divide by 100 to get decimal values

  //Current Sensor
  RawValue = analogRead(analogInCurrent);
  Vdc = (RawValue / 1024.0) * 5000; // Gets you mV
  Amps = ((Vdc - ACSoffset) / mVperAmp);

  //Print in Serial Monitor
  Serial.print("Voltage = ");
  Serial.print(voltage,3);
  Serial.print("\t Amps = "); // shows the voltage measured
  Serial.println(Amps,3);
  delay(1000);
}
