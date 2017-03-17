void printer(int no, int val)
{ 
  Serial.print("Value ");
  Serial.print(no);
  Serial.print(": ");
  Serial.print(val);
  Serial.print("\n");
}

const int MAX = 9;
int flexPin[] = {A0, A1,A2,A3,A4,A6,A7,A8,A9, A10, A11, A12, A14, A15};
int val[MAX];
void setup()
{
  Serial.begin(9600);
}
  
void loop()
{
  String s = "$ ";
  int value0 = analogRead(flexPin[0]); 
  for(int i=0 ; i<MAX ; i++)
    val[i] = analogRead(flexPin[i]);
//  Serial.println("Hello python buddy");
//  printer(1, /value0);
  for (int i=0 ; i<MAX ; i++)
    s += String(val[i])+" ";
  s += "$";
  Serial.println(s);
  delay(500);
} 
