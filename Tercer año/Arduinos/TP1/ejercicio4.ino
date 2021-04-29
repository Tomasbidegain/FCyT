#define rojo 11
#define pote1 A0

void setup()
{
  Serial.begin(9600);
  pinMode(rojo, OUTPUT);
}

void loop(){
  int valor = map(analogRead(pote1),0,1023,0,255);
  Serial.println(valor);
  analogWrite(rojo,valor);
}
 