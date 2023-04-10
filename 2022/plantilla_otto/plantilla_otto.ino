//----------------------------------------------------------------
//-- plantilla otto, maxi chaves
//-----------------------------------------------------------------
#include <Servo.h> 
#include <Otto.h>

Otto robot; //objeto Otto
Servo piernaI;  // Servo para pierna Izquierda
Servo piernaD;  // Servo para pierna Derecha
Servo pieI;  // Servo para pie Izquierdo
Servo pieD;  // Servo para pie Derecho
int buzzer=13;

void setup() {
  piernaI.attach(2);  // attaches the servo on pin 2 to the servo object 1
  piernaD.attach(3);  // attaches the servo on pin 3 to the servo object 2 
  pieI.attach(4);  // attaches the servo on pin 4 to the servo object 3
  pieD.attach(5);  // attaches the servo on pin 5 to the servo object 4 
  robot.init(2,3,4,5,true,13); //inicializo el otto
  pieD.write(45);
}

void loop() {
  piernaD.write(40);
  delay (500);
  pieD.write(120);
  delay (500);
  pieD.write(90);
  delay (500);
  piernaD.write(90);
  delay (700);
  piernaI.write(140);
  delay (500);
  pieI.write(60);
  delay (500);
  pieI.write(90);
  delay (500);
  piernaI.write(90);
  delay (700);

}
  
