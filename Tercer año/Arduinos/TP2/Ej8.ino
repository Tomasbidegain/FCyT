#define rojo 13
#define tilt 4
void setup()
{
  Serial.begin(9600);
  pinMode(rojo, OUTPUT);
  pinMode(tilt, INPUT);
}

void loop(){
  int val = digitalRead(tilt);
  Serial.println(val);
  if (val == HIGH){
    digitalWrite(rojo, HIGH);
    delay(300);
    digitalWrite(rojo, LOW);
  	delay(300);
  }
  else{
  	digitalWrite(rojo, LOW);
  }
}