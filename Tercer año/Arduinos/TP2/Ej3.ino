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
 if (valor_ldr > 366){
    digitalWrite(rojo, 250);
    delay(733);
   digitalWrite(rojo, 0);
 }	
 if (valor_ldr > 800){
    digitalWrite(rojo, 250);
    delay(733);
    digitalWrite(rojo, 0);
 }	
 if (valor_ldr > 1000){
    digitalWrite(rojo, 250);
    delay(733);
   	digitalWrite(rojo, 0);
 }
 if (valor_ldr > 1015){
    digitalWrite(rojo, 0);
    delay(2000);
 }
   if (valor_ldr > 1018){
    digitalWrite(rojo, 0);
    delay(2000);
 }
}