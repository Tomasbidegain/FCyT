#define rojo 13
#define verde 12
int flex = A0;
int data = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(flex, INPUT);
  pinMode(rojo, OUTPUT);
  pinMode(verde, OUTPUT);
}

void loop(){
  data = analogRead(flex);
  Serial.println(data);
  delay(2000);
  if (data < 770){
    digitalWrite(verde, 250);
    delay(2000);
  }
  if (data < 860){
    digitalWrite(verde, 10);
    delay(2000);
  }
  if (data > 880){
    digitalWrite(rojo, 10);
    delay(2000);
  }
  if (data >920){
    digitalWrite(rojo, 255);
    delay(2000);
  }
    digitalWrite(rojo, 0);
  	digitalWrite(verde, 0);
}