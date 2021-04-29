#define ldr A0
#define rojo 13
void setup()
{
  Serial.begin(9600);
  pinMode(rojo, OUTPUT);
}

void loop()
{
 int valor_ldr = analogRead(A0);
 Serial.println(valor_ldr);
 delay(1500);
 if (valor_ldr > 500){
    digitalWrite(rojo, 50);
    delay(2000);
 }	
 if (valor_ldr > 800){
    digitalWrite(rojo, 150);
    delay(2000);
 }	
 else if (valor_ldr > 1000){
    digitalWrite(rojo, 250);
    delay(2000);
 }
  else{
  	digitalWrite(rojo, LOW);
    delay(2000);
  }
}