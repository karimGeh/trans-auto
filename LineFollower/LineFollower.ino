  int vSpeed = 0;        // MAX 255
  int turn_speed = 100;    // MAX 255 
  int turn_delay = 10;

#define MAX_SPEED 200
int currentSpeedAIdx = 1;
int currentSpeedBIdx = 1;


//L293 Connection   
#define ENA 5
#define ENB 6
#define IN1 40
#define IN2 41
#define IN3 42
#define IN4 43


#define LIRS A0
#define CIRS A1
#define RIRS A2




int LIRSstate;
int RIRSstate;
int CIRSstate;

// Motors control 
void moveDriverMotors(int pinENA,int pinENB,int pinIN1,int pinIN2,int pinIN3,int pinIN4){
  analogWrite(ENA,pinENA);
  analogWrite(ENB,pinENB);
  digitalWrite(IN1,pinIN1);
  digitalWrite(IN2,pinIN2);
  digitalWrite(IN3,pinIN3);
  digitalWrite(IN4,pinIN4);
}
void forward(){ 
  moveDriverMotors(turn_speed,turn_speed,LOW,HIGH,HIGH,LOW);
  Serial.println("forward");
}

void left(){
   moveDriverMotors(MAX_SPEED,0,LOW,HIGH,LOW,HIGH);
  Serial.println("Left");
}

void right(){
  moveDriverMotors(0,MAX_SPEED,HIGH,LOW,HIGH,LOW);
  Serial.println("Right");
}

void Stop(){
  moveDriverMotors(0,0,LOW,LOW,LOW,LOW);
}
void setup() {
  pinMode(IN1,OUTPUT); 
  pinMode(IN2,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
  pinMode(ENA,OUTPUT);
  pinMode(ENB,OUTPUT);
  analogWrite(ENA,0);
  analogWrite(ENB,0);
  
  Serial.begin(9600);

  delay(3000);
  
}

void loop() {
  
  CIRSstate = analogRead(CIRS);
  LIRSstate = analogRead(LIRS);
  RIRSstate = analogRead(RIRS);

  Serial.print(LIRSstate);
  Serial.print("               ");
  Serial.print(CIRSstate);
  Serial.print("               ");
  Serial.print(RIRSstate);
  Serial.print("\n");
  
  
  if(RIRSstate > 500 && LIRSstate < 500)
  {
    Serial.println("turning right");
    right();
    delay(turn_delay);
  }
  if(RIRSstate < 500 && LIRSstate > 500)
  {
    Serial.println("turning left");
    left();
    delay(turn_delay);
  }

  if(RIRSstate < 500 && LIRSstate < 500)
  {
    Serial.println("going forward");
    forward();
    delay(turn_delay);
  }

  if(RIRSstate > 500 && LIRSstate > 500)
  { 
    Serial.println("stop");
    Stop();
  }

 
}










 
