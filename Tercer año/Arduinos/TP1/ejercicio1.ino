#define rojo 10
#define verde 9
#define amarillo 8

void setup()
{
  Serial.begin(9600);
  pinMode(rojo, OUTPUT);
  pinMode(verde, OUTPUT);
  pinMode(amarillo, OUTPUT);

}

void loop()
{
  digitalWrite(rojo, HIGH);
  delay(2000); 
  digitalWrite(rojo, LOW);
  delay(2000);
  digitalWrite(verde, HIGH);
  delay(2000); 
  digitalWrite(verde, LOW);
  delay(2000); 
  digitalWrite(amarillo, HIGH);
  delay(2000); 
  digitalWrite(amarillo, LOW);
  delay(2000); 
}