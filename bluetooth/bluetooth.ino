const int ProxSensor=A0;
int inputVal1 = 0;
const int ProxSensor=A0;
int inputVal1 = 0;
const int ProxSensor=A0;
int inputVal1 = 0;

void setup() 
{                        // Pin 13 has an LED connected on most Arduino boards:  
  pinMode(ProxSensor,INPUT);    //Pin 2 is connected to the output of proximity sensor
  Serial.begin(9600);
}

void loop() 
{
inputVal = analogRead(ProxSensor);
Serial.println(inputVal);
delay(1000);              // wait for a second
}
