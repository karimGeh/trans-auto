#include <SoftwareSerial.h>
SoftwareSerial HC05(19, 11); //HC06-TX Pin 10, HC06-RX to Arduino Pin 11

int LED = 7; //Use whatever pins you want 

void setup() {
  Serial.begin(9600);
  HC05.begin(9600); //Baudrate 9600 , Choose your own baudrate 
  pinMode(LED, OUTPUT);
}

void loop() {
  if(HC05.available() > 0) //When HC06 receive something
  {
    
   Serial.println(HC05.available());
    char receive = HC05.read(); //Read from Serial Communication
    if(receive == '1') //If received data is 1, turn on the LED and send back the sensor data
    {
      Serial.println(receive);
      digitalWrite(LED, HIGH); 
    }
    else digitalWrite(LED, LOW);//If received other data, turn off LED
  }

}