#include <Servo.h>
Servo motor;
int cont = 0;

void setup()
{
  Serial.begin(9600);
  motor.attach(3);
}

void loop(){
  	int num = random(0,180);
	motor.write(num);
  	delay(1500);
  	cont = cont + 1;
  	Serial.print("Grados:");
  	Serial.println(num);
  	if (cont == 3){
  	  Serial.println("La posicion en la que quedo el servo motor es :");
      Serial.println(num);
      Serial.println("Moviendo a 0 grados");
      motor.write(0);
      delay(1500);
      Serial.println("Moviendo a 180 grados");
      motor.write(180);
      delay(1500);
      Serial.println("Moviendo a 90 grados");
      motor.write(90);
      delay(1500);
    }
}