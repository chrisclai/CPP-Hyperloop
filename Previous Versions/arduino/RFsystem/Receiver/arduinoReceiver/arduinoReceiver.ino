#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

RF24 radio(9, 10); // CE, CSN         
const byte address[6] = "00001";     //Byte of array representing the address. This is the address where we will send the data. This should be same on the receiving side.

void setup() {
  Serial.begin(115200);
  radio.begin();                  //Starting the Wireless communication
  radio.openReadingPipe(0, address); //Setting the address where we will send the data
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();
}

void loop() {
  String msg = "";
  if (radio.available()) {
    radio.read(&msg, sizeof(msg));
    Serial.println(msg);
    delay(50);
  }
}
