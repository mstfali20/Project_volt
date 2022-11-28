
int analogInput = A0;
int analogInput2 = A1;
int analogInput3 = A2;
float vout = 0.0;
float vout2 = 0.0;
float vout3 = 0.0;
float vin = 0.0;
float vin2 = 0.0;
float vin3 = 0.0;
float R1 = 10000.0; // 100K ohm direnç
float R2 = 1000.0; // 10K ohm direnç
float R12 = 22.0; // 100K ohm direnç
float R22 = 10.0; // 10K ohm direnç
int value = 0;
int value2 = 0;
int value3 = 0;
void setup(){
   pinMode(analogInput, INPUT);
   pinMode(analogInput2, INPUT);
   pinMode(analogInput3 , INPUT);
   Serial.begin(9600);
 
}
void loop(){
   // read the value at analog input
   value = analogRead(analogInput);
   vout = (value * 5.0) / 1024.0; 
   vin = vout / (R2/(R1+R2)); 
   if (vin<0.09) {
      vin=0.0;
   }
   Serial.print(vin);
   Serial.println(" volt");
   delay(1000);
   
   value2 = analogRead(analogInput2);
   vout2 = (value2 * 5.0) / 1024.0; 
   vin2= vout2 / (R22
   /(R12+R22)); 
   if (vin2<0.09) {
      vin2=0.0;
   }
   Serial.print(vin2);
   Serial.println(" volt2");
   delay(1000);

   value3 = analogRead(analogInput3);
   vout3 = (value3 * 5.0) / 1024.0; 
   vin3= vout3 / (R2/(R1+R2)); 
   if (vin3<0.09) {
      vin3=0.0;
   }
   Serial.print(vin3);
   Serial.println(" volt3");
   delay(1000);   
}
