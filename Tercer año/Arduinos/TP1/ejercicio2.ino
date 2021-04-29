#define rojo 10
#define verde 9
#define amarillo 8

void setup()
{
  Serial.begin(9600);
  pinMode(rojo, OUTPUT);
  pinMode(verde, OUTPUT);
  pinMode(amarillo, OUTPUT);
  randomSeed(analogRead(0));

}

void loop(){
  int numero = random(1, 10);
  Serial.println(numero);
  cambiar_color(numero);
}

void cambiar_color(int numero){
    if (numero == 1 || numero == 3 || numero == 7) {
        digitalWrite(rojo, HIGH);
        delay(2000); 
        digitalWrite(rojo, LOW);
        delay(2000);
    }
 	else if (numero == 6 || numero == 2|| numero == 8){
        digitalWrite(verde, HIGH);
        delay(2000); 
        digitalWrite(verde, LOW);
        delay(2000); 
    }
  	else if (numero == 4 || numero == 5|| numero == 9){
    	digitalWrite(amarillo, HIGH);
    	delay(2000); 
     	digitalWrite(amarillo, LOW);
    	delay(2000); 
	}
  	else{
      digitalWrite(verde, LOW);
      digitalWrite(rojo, LOW);
      digitalWrite(amarillo, LOW);
  	}
}