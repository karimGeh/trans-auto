/*
 * 
 * All the resources for this project : https://github.com/karimGeh/trans-auto
 * 
 * Created by KARIM GEHAD
 * Github : https://github.com/karimGeh
 * LinkedIn : https://www.linkedin.com/in/karim-gehad-913237149/
 * Email : karim2jihad@gmail.com
 * 
 */

 
// C library
  #include <stdio.h>


// Arduino library
  #include <SPI.h>
  #include <MFRC522.h>


// Gears
  #define GEAR0 0
  #define GEAR1 100
  #define GEAR2 125
  #define GEAR3 150
  #define GEAR4 175
  #define GEAR5 200

//RFID PINS
  #define SDA 10
  #define RST 9

// DRIVER PINS
  #define ENA 5
  #define ENB 6
  #define IN1 40
  #define IN2 41
  #define IN3 42
  #define IN4 43

// IR PINS
  #define LeftIRS A8
  #define CenterIRS A9
  #define RightIRS A10

// Bluetooth Connection
  #define CNX 45

// Ultrasonic
  #define Trig 3
  #define Echo 2




  int RobotState = 0;
  int executionL = 0;
  int executionR = 0;

// declaration
  MFRC522 rfid(SDA, RST);

// Needed variabl
  char data;
  char Buffer[50];
  
  int LIRSstate;
  int RIRSstate;

// Ultrasonic variable
  long duration;
  int distance;


//Functions
  // Move the motors based on argument
void moveDriverMotors(int SpeedA,int SpeedB,int pinIN1,int pinIN2,int pinIN3,int pinIN4){
  analogWrite(ENA,SpeedA);
  analogWrite(ENB,SpeedB);
  digitalWrite(IN1,pinIN1);
  digitalWrite(IN2,pinIN2);
  digitalWrite(IN3,pinIN3);
  digitalWrite(IN4,pinIN4);
}

void TurnLeftFixedPosition(int MOTORS_SPEED){
   moveDriverMotors(MOTORS_SPEED,MOTORS_SPEED,LOW,HIGH,LOW,HIGH);
  Serial.println("Left fixed position");
}

void TurnRightFixedPosition(int MOTORS_SPEED){
  moveDriverMotors(MOTORS_SPEED,MOTORS_SPEED,HIGH,LOW,HIGH,LOW);
  Serial.println("Right fixed position");
}

void STOPMOTORS(){
  moveDriverMotors(0,0,LOW,LOW,LOW,LOW);
  Serial.println("Stop Motors");
}

void ForwardLineFollower(int MOTORS_SPEED){ 
  moveDriverMotors(MOTORS_SPEED,MOTORS_SPEED,LOW,HIGH,HIGH,LOW);
  Serial.println("Forward Line Follower");
}

void TurnLeftLineFollower(int MOTORS_SPEED){
   moveDriverMotors(MOTORS_SPEED,0,LOW,HIGH,LOW,HIGH);
  Serial.println("Left Line Follower");
}

void TurnRightLineFollower(int MOTORS_SPEED){
  moveDriverMotors(0,MOTORS_SPEED,HIGH,LOW,HIGH,LOW);
  Serial.println("Right Line Follower");
}
// Setup
void setup() {
  // initialize Serial
    Serial.begin(9600);
    Serial1.begin(9600);
  
  // initialize SPI bus
    SPI.begin();
    
  // intialize RFID
    rfid.PCD_Init();

  // initialize pins
    pinMode(CNX,INPUT); 
    pinMode(IN1,OUTPUT); 
    pinMode(IN2,OUTPUT);
    pinMode(IN3,OUTPUT);
    pinMode(IN4,OUTPUT);
    pinMode(ENA,OUTPUT);
    pinMode(ENB,OUTPUT);

  // initialize Ultrasonic
    pinMode(Trig, OUTPUT);
    pinMode(Echo, INPUT); 

      
  // Stop Motors
    analogWrite(ENA,0);
    analogWrite(ENB,0);
}


// program
void loop() {
  // immediately stop the motors once the robot is not connected
  if(!digitalRead(CNX)){
    STOPMOTORS();
    delay(1000);
    return;
  }

  // distance calculation
    digitalWrite(Trig, LOW);
    delayMicroseconds(2);
    digitalWrite(Trig, HIGH);
    delayMicroseconds(10);
    digitalWrite(Trig, LOW);

    duration = pulseIn(Echo, HIGH);
    
    distance= duration*0.034/2;

    if(distance <= 50 ){
      STOPMOTORS();
      delay(1000);
      return;
    }

  
  // connection succeded
  Serial.println("connection succeded");
    if(Serial1.available() > 0){
      data = Serial1.read();
      Serial.println(data);
      delay(1000);
      if(data == 'A') RobotState = 0;
      if(data == 'B') RobotState = 1;
      if(data == 'C') RobotState = 2;
      if(data == 'N') {
        ForwardLineFollower(GEAR1);
        RobotState = 1;
      }
      if(data == 'R'){
        TurnRightFixedPosition(GEAR3);
        RobotState = 2;
        executionR = 1;
      }
      if(data == 'L'){
        TurnLeftFixedPosition(GEAR3);
        RobotState = 2;
        executionL = 1;
      }
    }
  // Robot State == 0
    if(RobotState == 0) {
      Serial.println("RobotState == 0");
      STOPMOTORS();
    }

  Serial.println(RobotState);
  // IR conditioning
    Serial.println("IR conditioning");
    LIRSstate = analogRead(LeftIRS);
    RIRSstate = analogRead(RightIRS);

    // Line Follower
    if(RobotState == 1){
      Serial.println("Line Follower ---- RobotState == 1");
      if((LIRSstate > 500 && RIRSstate > 500) || LIRSstate < 500 && RIRSstate < 500) ForwardLineFollower(GEAR1) ;
      if(RIRSstate > 500 && LIRSstate < 500) TurnRightLineFollower(GEAR2);
      if(RIRSstate < 500 && LIRSstate > 500) TurnLeftLineFollower(GEAR2);
    }

    // Server Control
    if(RobotState == 2){
      Serial.println("Server Control ---- RobotState == 2");
      if(executionR > 0){
        if(RIRSstate > 500 && executionR == 1) executionR = 2;
        if(RIRSstate < 500 && executionR == 2){          
          delay(100);
          executionR = 0;
          STOPMOTORS();
          RobotState = 1;          
          delay(100);
        }
      }
      if(executionL > 0){
        if(LIRSstate > 500 && executionL == 1) executionL = 2;
        if(LIRSstate < 500 && executionL == 2){
          delay(100);
          executionL = 0;
          STOPMOTORS();
          RobotState = 1;
          delay(100);
        }
      }
    }


  // RFID CODE
    Serial.println("RFID CODE");
    if ( !rfid.PICC_IsNewCardPresent())  return;
    if ( !rfid.PICC_ReadCardSerial())    return;

    // if the code arrives here then an NFC CARD has been detected
      STOPMOTORS();
      RobotState = 0;
      sprintf(Buffer,"%d %d %d %d",rfid.uid.uidByte[0],rfid.uid.uidByte[1],rfid.uid.uidByte[2],rfid.uid.uidByte[3]);
      Serial.println(Buffer);
      Serial1.print(Buffer);
      Serial1.print("\n");

    // Re-Init RFID
      rfid.PICC_HaltA(); // Halt PICC
      rfid.PCD_StopCrypto1(); // Stop encryption on PCD
  

}
