

//Constants:

const int flexPin0 = A0;   //pin 3 has PWM funtion

const int flexPin1 = A1; //pin A0 to read analog input



//Variables:

void setup(){
  
 //Set pin 3 as 'output'

  Serial.begin(9600);       //Begin serial communication

}

void printer(int no, int val)
{
  Serial.print("Value ");
  Serial.print(no);
  Serial.print(": ");
  Serial.print(val);
  Serial.print("\n");
}

void loop(){

  

  int value0 = analogRead(flexPin0);         //Read and save analog value from potentiometer
  int value1 = analogRead(flexPin1);
  printer(0, value0);
//  printer(1, /Svalue1);
  //Print value1

  //value = map(value, 700, 900, 0, 255);//Map value 0-1023 to 0-255 (PWM)
  
  //Serial.println(value);               //Print value

  //analogWrite(ledPin, value);          //Send PWM value to led

  delay(500);                          //Small delay

  

}
