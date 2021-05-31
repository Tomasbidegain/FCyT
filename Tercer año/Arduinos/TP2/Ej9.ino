#define pul 2
#define rojo 13
#define azul 12
#define verde 8
void setup() {
  Serial.begin(9600);
  pinMode(pul, INPUT_PULLUP);
  pinMode(rojo, OUTPUT);
  pinMode(azul, OUTPUT);
  pinMode(verde, OUTPUT);
}

void loop() {
  int numero = 0;
  int sensorVal = digitalRead(pul);
  Serial.println(sensorVal);
  if (sensorVal == 1){
    numero = random(1,4);
    Serial.println(numero);
   	if (numero == 1){
      digitalWrite(rojo, HIGH);
      delay(2000);
      digitalWrite(rojo, LOW);
    }
    if (numero == 2){
      digitalWrite(azul, HIGH);
      delay(2000);
      digitalWrite(azul, LOW);
    }
    if (numero == 3){
      digitalWrite(verde, HIGH);
      delay(2000);
      digitalWrite(verde, LOW);
    }
  }
  if(sensorVal == 0){
    digitalWrite(rojo, LOW);
    digitalWrite(azul, LOW);
    digitalWrite(verde, LOW);
  }
}