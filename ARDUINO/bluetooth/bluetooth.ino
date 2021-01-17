char data;
void setup() {
   Serial.begin(9600);
  Serial1.begin(9600);

}

void loop() {
   if(Serial1.available() > 0)
   {
      data = Serial1.read();
      Serial.println(data);}

}
