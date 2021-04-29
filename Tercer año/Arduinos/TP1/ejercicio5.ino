#define rojo 11
#define azul 10
#define verde 9
#define pote1 A0

void setup()
{
  Serial.begin(9600);
  pinMode(rojo, OUTPUT);
  pinMode(azul, OUTPUT);
  pinMode(verde, OUTPUT);
}

void loop(){
  Serial.println("combinacion verde con rojo");
  digitalWrite(verde,HIGH);
  int valor = map(analogRead(pote1),0,1023,0,255);
  Serial.println(valor);
  analogWrite(rojo,valor);
  delay(3000);
  valor = map(analogRead(pote1),0,1023,0,255);
  Serial.println(valor);
  analogWrite(rojo,valor);
  delay(3000);
  valor = map(analogRead(pote1),0,1023,0,255);
  Serial.println(valor);
  analogWrite(rojo,valor);
  delay(2000);
  digitalWrite(verde, LOW);
  analogWrite(rojo, LOW);

  
  Serial.println("combinacion verde con azul");
  digitalWrite(verde,HIGH);
  valor = map(analogRead(pote1),0,1023,0,255);
  Serial.println(valor);
  analogWrite(azul,valor);
  delay(3000);
  valor = map(analogRead(pote1),0,1023,0,255);
  Serial.println(valor);
  analogWrite(azul,valor);
  delay(3000);
  valor = map(analogRead(pote1),0,1023,0,255);
  Serial.println(valor);
  analogWrite(azul,valor);
  delay(2000);
  digitalWrite(verde, LOW);
  analogWrite(azul, LOW);

  
  Serial.println("Combinacion azul con rojo");
  digitalWrite(azul,HIGH);
  valor = map(analogRead(pote1),0,1023,0,255);
  Serial.println(valor);
  analogWrite(rojo,valor);
  delay(3000);
  valor = map(analogRead(pote1),0,1023,0,255);
  Serial.println(valor);
  analogWrite(rojo,valor);
  delay(3000);
  valor = map(analogRead(pote1),0,1023,0,255);
  Serial.println(valor);
  analogWrite(rojo,valor);
  delay(2000);
  digitalWrite(azul, LOW);
  analogWrite(rojo, LOW);
  
}