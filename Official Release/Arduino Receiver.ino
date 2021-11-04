// constants won't change. They're used here to set pin numbers:
const int LED = 2;  // the number of the pushbutton pin
void setup()
{
  Serial.begin(115200);
  // initialize the pushbutton pin as an input:
  pinMode(LED, OUTPUT);
}
void loop()
{
  if (Serial.available() > 0){
    // reads and converts the serial as a character from python to C++
    char command = Serial.read();
    if (command == 'x')
    {
      // changes led light on when command is x
      digitalWrite(LED, HIGH);
    }
    else if (command == 'o')
    {
      // changes led light off when command is o 
      digitalWrite(LED, LOW);

    }
  }
}
