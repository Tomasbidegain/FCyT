#define ecoPin 8
#define trigPin 9
#define rojo 13
#define azul 12
#define verde 11
void setup()
{
 Serial.begin(9600);
 pinMode(ecoPin, INPUT);
 pinMode(trigPin, OUTPUT);
 pinMode(rojo, OUTPUT);
 pinMode(azul, OUTPUT);
 pinMode(verde, OUTPUT); 
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
  
  if(cm < 5){ // rojo
    analogWrite(rojo, 255);
  }
  else if(cm < 10){ // anaranjado
    analogWrite(rojo, 255);
    analogWrite(verde, 30);
  }
  else if(cm < 25){ // amarillo
    analogWrite(rojo, 255);
    analogWrite(verde, 255);
  }
  else{
    analogWrite(rojo, 0);
    analogWrite(verde, 0);
  }
  
}