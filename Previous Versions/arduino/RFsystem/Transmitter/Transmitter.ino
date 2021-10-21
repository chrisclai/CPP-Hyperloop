#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(9, 10); // CE, CSN         
const byte address[6] = "00001";     //Byte of array representing the address. This is the address where we will send the data. This should be same on the receiving side.

#define DCMotor 2
#define brakeLED 4

// [Function] Checks to see if serial data has been recieved from the Raspberry Pi
String RPiSerial()
{
  if (Serial.available() > 0)
  {
    String command = String(Serial.read());
    return command;
  }
}

void setup() {
  Serial.begin(115200);
  radio.begin();                  //Starting the Wireless communication
  radio.openWritingPipe(address); //Setting the address where we will send the data
  radio.setPALevel(RF24_PA_MIN);  //You can set it as minimum or maximum depending on the distance between the transmitter and receiver.
  radio.stopListening();          //This sets the module as transmitter

  pinMode(brakeLED, OUTPUT);
  digitalWrite(brakeLED, LOW);

  pinMode(DCMotor, OUTPUT);
  digitalWrite(DCMotor, LOW);
}

void loop()
{
  // Send the whole data from the structure to the receiver
  String packet = RPiSerial();
  radio.write(&packet, sizeof(packet));
}
