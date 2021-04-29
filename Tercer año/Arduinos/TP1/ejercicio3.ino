#define rojo 10
#define verde 9
#define azul 8

void setup()
{
  Serial.begin(9600);
  pinMode(rojo, OUTPUT);
  pinMode(verde, OUTPUT);
  pinMode(azul, OUTPUT);
  randomSeed(analogRead(0));

}

void loop(){
  int numero = random(1, 8);
  Serial.println(numero);
  cambiar_color(numero);
}

void cambiar_color(int numero){
  switch (numero) {
  case 1:
    //rojo
    digitalWrite(rojo, HIGH);
    delay(2000); 
    digitalWrite(rojo, LOW);
    delay(2000);
    break;
  case 2:
    //verde
    digitalWrite(verde, HIGH);
    delay(2000); 
    digitalWrite(verde, LOW);
    delay(2000); 
    break;
  case 3:
  	//azul
    digitalWrite(azul, HIGH);
    delay(2000); 
    digitalWrite(azul, LOW);
    delay(2000); 
  	break;
  case 4:
  	//amarillo
    digitalWrite(rojo, HIGH);
    digitalWrite(verde, HIGH);
    delay(2000);
    digitalWrite(rojo, LOW);
    digitalWrite(verde, LOW);
    delay(2000);
    break;
  case 5:
  	//violeta
    digitalWrite(rojo, HIGH);
    digitalWrite(azul, HIGH);
    delay(2000);
    digitalWrite(rojo, LOW);
    digitalWrite(azul, LOW);
    delay(2000);
    break;
  case 6:
  	//celeste
    digitalWrite(azul, HIGH);
    digitalWrite(verde, HIGH);
    delay(2000);
    digitalWrite(azul, LOW);
    digitalWrite(verde, LOW);
    delay(2000);
    break;    
  case 7:
  	//blanco
      digitalWrite(verde, HIGH);
      digitalWrite(rojo, HIGH);
      digitalWrite(azul, HIGH);
      delay(2000);
	  digitalWrite(verde, LOW);
      digitalWrite(rojo, LOW);
      digitalWrite(azul, LOW);    
      delay(2000);
  	break;
  case 8:
  	//apagado
	  digitalWrite(verde, LOW);
      digitalWrite(rojo, LOW);
      digitalWrite(azul, LOW);
      delay(2000);
  	break;
 }
}
  