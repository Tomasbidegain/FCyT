#include <Servo.h>
#define pote1 A0
Servo motor;

void setup()
{
  Serial.begin(9600);
  motor.attach(3);
  pinMode(pote1, INPUT);
}

void loop(){
  	int valor = map(analogRead(pote1),0,1023,0,180);
  	Serial.println(valor);//grado para el servo motor
	motor.write(valor);
  	delay(1500);
}