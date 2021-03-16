#define DCMotor 6
#define brakeLED1 7
#define brakeLED2 8

// [Function] Checks to see if serial data has been recieved from the Raspberry Pi
void RPiSerial()
{
  if (Serial.available() > 0)
  {
    char command = Serial.read();
    // Currently, if string recieved == "brakeon", turn LED on, vice versa for off
    if (command == 'a')
    {
      digitalWrite(brakeLED1, HIGH);
      digitalWrite(brakeLED2, HIGH);
      //return "brakeon";
    }
    else if (command == 'b')
    {
      digitalWrite(brakeLED1, LOW);
      digitalWrite(brakeLED2, LOW);
      //return "brakeoff";
    }
    else if (command == 'y')
    {
      digitalWrite(DCMotor, HIGH);
      //return "motoron";
    }
    else if (command == 'z')
    {
      digitalWrite(DCMotor, LOW);
      //return "motoroff";
    }
  }
}

void setup() {
  Serial.begin(115200);

  pinMode(brakeLED1, OUTPUT);
  digitalWrite(brakeLED1, LOW);

  pinMode(brakeLED2, OUTPUT);
  digitalWrite(brakeLED2, LOW);

  pinMode(DCMotor, OUTPUT);
  digitalWrite(DCMotor, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  RPiSerial();
}
