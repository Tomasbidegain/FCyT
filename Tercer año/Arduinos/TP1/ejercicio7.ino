#define ecoPin 8
#define trigPin 9
void setup()
{
 Serial.begin(6900);
 pinMode(ecoPin, INPUT);
 pinMode(trigPin, OUTPUT);
}

void loop()
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  int duration = pulseIn(ecoPin, HIGH);

  double cm = duration*0.034/2;
  Serial.print("Distance: ");
  Serial.print(cm);
  Serial.println(" cm");

  delay(250);
}