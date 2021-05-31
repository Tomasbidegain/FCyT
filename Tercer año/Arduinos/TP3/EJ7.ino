#include <LiquidCrystal.h>
LiquidCrystal lcd(2,3,4,5,6,7);
#define ecoPin 8
#define trigPin 9
#define rojo 13
void setup()
{
 Serial.begin(9600);
 pinMode(ecoPin, INPUT);
 pinMode(trigPin, OUTPUT);
 pinMode(rojo, OUTPUT);
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
  
  lcd.begin(16,2);
  lcd.setCursor(0,0);
  lcd.print("Distancia:");
  lcd.setCursor(11,0);
  lcd.print(cm);

  if(cm < 5){
  	lcd.setCursor(0,1);
    lcd.print("MUY CERCA");
    delay(5000);
  }
  if(cm < 10){
    lcd.setCursor(0,1);
    lcd.print("CERCA");
    delay(5000);
  }
  if(cm < 25){
    lcd.setCursor(0,1);
    lcd.print("PROXIMO");
    delay(5000);    
  }
  if(cm > 25){
    lcd.setCursor(0,1);
  }
}