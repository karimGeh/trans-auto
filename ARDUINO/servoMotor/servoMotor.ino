#include <Servo.h> 
// Declare the Servo pin 
Servo servo_test1; 
Servo servo_test2; //initialize a servo object for the connected servo  
                
int angle = 0;    
 
void setup() 
{ 
  servo_test1.attach(9);
  servo_test2.attach(10);// attach the signal pin of servo to pin9 of arduino
} 
  
void loop() 
{ 
  servo_test1.write(0);
  

 
  delay(1000);
  
  servo_test1.write(90);

 delay(1000);
}
