#define pir 2
#define rojo 13
#define azul 12
void setup() {
  Serial.begin(9600);
  pinMode(pir, INPUT);
  pinMode(rojo, OUTPUT);
  pinMode(azul, OUTPUT);
}

void loop() {
  int val = digitalRead(pir);
  Serial.println(val);
  if (val == HIGH) {
    digitalWrite(rojo, HIGH);
    delay(200);
	digitalWrite(rojo, 0);
  	delay(200);
  }
  else{
  	digitalWrite(azul, HIGH);
    delay(200);
	digitalWrite(azul, 0);
  	delay(200);
  }
}