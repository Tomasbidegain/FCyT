#include <Servo.h>
Servo motor;

void setup()
{
  Serial.begin(9600);
  motor.attach(3);
}

void loop(){
  	int num = random(0,180);
  	Serial.println(num);//grado para el servo motor
	motor.write(num);
  	delay(1500);
}