#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(9, 10); // CE, CSN         
const byte address[6] = "00001";     //Byte of array representing the address. This is the address where we will send the data. This should be same on the receiving side.

#define DCMotor 2
#define brakeLED 4

// [Function] Checks to see if serial data has been recieved from the Raspberry Pi
void RPiSerial()
{
  if (Serial.available() > 0)
  {
    char command = Serial.read();
    // Currently, if string recieved == "brakeon", turn LED on, vice versa for off
    if (command == 'a')
    {
      digitalWrite(brakeLED, HIGH);
    }
    else if (command == 'b')
    {
      digitalWrite(brakeLED, LOW);
    }
    else if (command == 'y')
    {
      digitalWrite(DCMotor, HIGH);
    }
    else if (command == 'z')
    {
      digitalWrite(DCMotor, LOW);
    }
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
  radio.write(&packet, sizeof(CMD_Packet));
}
