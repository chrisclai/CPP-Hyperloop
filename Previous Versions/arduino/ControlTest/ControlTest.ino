const int solenoid = 7;
const int motor = 8;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(solenoid, OUTPUT);
  pinMode(motor, OUTPUT);
  digitalWrite(solenoid, LOW);
  digitalWrite(motor, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("SOLENOID TESTING");
  digitalWrite(solenoid, HIGH);
  delay(5000);
  digitalWrite(solenoid, LOW);
  delay(5000);
  Serial.println("MOTOR TESTING");
  digitalWrite(motor, HIGH);
  delay(3000);
  digitalWrite(motor, LOW);
  delay(3000);
}
