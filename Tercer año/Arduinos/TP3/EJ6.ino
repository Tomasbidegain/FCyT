#define ecoPin 8
#define trigPin 9
#define bip 3
void setup()
{
 Serial.begin(9600);
 pinMode(ecoPin, INPUT);
 pinMode(trigPin, OUTPUT);
 pinMode(bip, OUTPUT);
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
  
  if ((cm > 20) && (cm < 30)){
	tone(bip,700,250);
    delay(1500);
  }
  if ((cm > 12) && (cm < 20)){
    tone(bip,700,250);
    delay(1000);
  }
  if ((cm > 6) && (cm < 12)){
    tone(bip,700,250);
    delay(500);
  }
  if ((cm > 2) && (cm < 6)){
    tone(bip,700,250);
    delay(200);
  }
}