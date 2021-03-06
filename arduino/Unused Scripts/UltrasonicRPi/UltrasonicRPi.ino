// Project: Ultrasonic Sensor Data to RPi for CPP Hyperloop 2020
// Author: Christopher Lai
// Version Control: 10.22.2020 12:16:45AM

const int pingPin = 8;
const int echoPin = 7;

void setup() {
   Serial.begin(9600);
}

void loop() {
   long duration, cm;
   pinMode(pingPin, OUTPUT);
   digitalWrite(pingPin, LOW);
   delayMicroseconds(2);
   digitalWrite(pingPin, HIGH);
   delayMicroseconds(10);
   digitalWrite(pingPin, LOW);
   pinMode(echoPin, INPUT);
   duration = pulseIn(echoPin, HIGH);
   cm = microsecondsToCentimeters(duration);
   Serial.println(cm);
   delay(100);
}

long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}
