#define NB_CARDS 4
#include <SPI.h> // SPI
#include <MFRC522.h> // RFID
#include <stdio.h>

#define SPEED_LVL_0 0
#define SPEED_LVL_1 100
#define SPEED_LVL_2 125
#define SPEED_LVL_3 150
#define SPEED_LVL_4 200
#define SPEED_LVL_5 250


#define CNX 44

//RFID PINS
#define SS_PIN 10
#define RST_PIN 9

//DRIVER PINS
#define ENA 5
#define ENB 6
#define IN1 40
#define IN2 41
#define IN3 42
#define IN4 43


// Déclaration 
MFRC522 rfid(SS_PIN, RST_PIN); 

// Tableau contentent l'ID
char data = 0;
char Buffer[50];
byte nuidPICC[4];

int Speeds[6] = {SPEED_LVL_0,SPEED_LVL_1,SPEED_LVL_2,SPEED_LVL_3,SPEED_LVL_4,SPEED_LVL_5};

int currentSpeedAIdx = 1;
int currentSpeedBIdx = 1;
typedef byte card[4];
card cartes[NB_CARDS] { //Déclaration
{58,238,102,26}, //1ère carte
//{69,187,172,32},
{69,187,172,32}, //2ème carte
{122,49,132,128}, //3ème carte
{187,7,122,89} //4ème carte

}; //Fin du tableau.
byte i;
    

byte GetAccesState(byte *CodeAcces,byte *NewCode) 
{
  if ((CodeAcces[0]==NewCode[0])&&(CodeAcces[1]==NewCode[1])&&
  (CodeAcces[2]==NewCode[2])&& (CodeAcces[3]==NewCode[3]))
    return 1; 
  else
    return 0; 
}

void moveDriverMotors(int pinENA,int pinENB,int pinIN1,int pinIN2,int pinIN3,int pinIN4){
  analogWrite(ENA,pinENA);
  analogWrite(ENB,pinENB);
  digitalWrite(IN1,pinIN1);
  digitalWrite(IN2,pinIN2);
  digitalWrite(IN3,pinIN3);
  digitalWrite(IN4,pinIN4);
}
void forward(int SPEED_A,int SPEED_B){ 
  moveDriverMotors(SPEED_A,SPEED_B,LOW,HIGH,HIGH,LOW);
  Serial.println("forward");
}
 
void back(int SPEED_A,int SPEED_B){
  moveDriverMotors(SPEED_A,SPEED_B,HIGH,LOW,LOW,HIGH);
  Serial.println("Back");
}
 
void left(int SPEED_A,int SPEED_B){
   moveDriverMotors(SPEED_A,SPEED_B,LOW,HIGH,LOW,HIGH);
  Serial.println("Left");
}

void right(int SPEED_A,int SPEED_B){
  moveDriverMotors(SPEED_A,SPEED_B,HIGH,LOW,HIGH,LOW);
  Serial.println("Right");
}

void Stop(){
  moveDriverMotors(0,0,LOW,LOW,LOW,LOW);
}

void setup() 
{ 
  // Init RS232
  Serial.begin(9600);
  Serial3.begin(9600);
  // Init SPI bus
  SPI.begin();
  // Init MFRC522 
  rfid.PCD_Init();
  //Init pins
  pinMode(CNX,INPUT); 
  pinMode(IN1,OUTPUT); 
  pinMode(IN2,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
  pinMode(ENA,OUTPUT);
  pinMode(ENB,OUTPUT);
  analogWrite(ENA,0);
  analogWrite(ENB,0);
}
 
void loop() 
{
  
  if(Serial3.available() > 0)
   {
      data = Serial3.read();
      Serial.println(data);
      if(data == 'N')
      {
        forward(Speeds[currentSpeedAIdx],Speeds[currentSpeedBIdx]);
      }
      else if(data == 'S')
      {
        back(Speeds[currentSpeedAIdx],Speeds[currentSpeedBIdx]);
      }   
      else if(data == 'R')
      {
        right(Speeds[currentSpeedAIdx],Speeds[currentSpeedBIdx]);
      }
      else if(data == 'L')
      {
        left(Speeds[currentSpeedAIdx],Speeds[currentSpeedBIdx]);
      }
      else if(data == '0')
      {
        Stop();
      }
      else if(data == 'U')
      {
        currentSpeedAIdx++;
        if(currentSpeedAIdx == 5)
          currentSpeedAIdx--;
      }
      else if(data == 'D')
      {
        currentSpeedAIdx--;
        if(currentSpeedAIdx == -1)
          currentSpeedAIdx++;
      }
      else if(data == 'V')
      {
        currentSpeedBIdx++;
        if(currentSpeedBIdx == 5)
          currentSpeedBIdx--;
      }
      else if(data == 'E')
      {
        currentSpeedBIdx--;
        if(currentSpeedBIdx == -1)
          currentSpeedBIdx++;
      }
   }
  // Initialisé la boucle si aucun badge n'est présent 
  if ( !rfid.PICC_IsNewCardPresent())
    return;

  // Vérifier la présence d'un nouveau badge 
  if ( !rfid.PICC_ReadCardSerial())
    return;
  
  // Enregistrer l'ID du badge (4 octets) 
  Stop();
  for (byte i = 0; i < 4; i++) 
  {
    nuidPICC[i] = rfid.uid.uidByte[i];
  }
  if(digitalRead(CNX)){
    sprintf(Buffer,"%d %d %d %d",nuidPICC[0],nuidPICC[1],nuidPICC[2],nuidPICC[3]);
    Serial.println(Buffer);
    Serial3.print(Buffer);
    Serial3.print("\n");
  }
 // Affichage de l'ID 
  /*Serial.println("Un badge est détecté");
  Serial.println(" L'UID du tag est:");
  for (i = 0; i < 4; i++) 
  {
    Serial.print(nuidPICC[i], HEX);
    Serial.print(" ");
  }
  
  Serial.println();*/
//Taches à faire
    /*if (GetAccesState(cartes[0],nuidPICC))
    {
     forward(Speeds[currentSpeedAIdx],Speeds[currentSpeedBIdx]);
      //delay(pause);
       //Stop();
    }
    else if (GetAccesState(cartes[1],nuidPICC))
    {
     
      back(Speeds[currentSpeedAIdx],Speeds[currentSpeedBIdx]);
      //delay(pause);
      //Stop();
    }
    else if (GetAccesState(cartes[2],nuidPICC))
    {
       right(Speeds[currentSpeedAIdx],Speeds[currentSpeedBIdx]);
       //delay(pause);
       //Stop();
    }
    else if (GetAccesState(cartes[3],nuidPICC))
    {
       left(Speeds[currentSpeedAIdx],Speeds[currentSpeedBIdx]);
       //delay(pause);
       //Stop();
    }
    else
    Serial.println("Invalide Card");*/
  // Re-Init RFID
  rfid.PICC_HaltA(); // Halt PICC
  rfid.PCD_StopCrypto1(); // Stop encryption on PCD
}
