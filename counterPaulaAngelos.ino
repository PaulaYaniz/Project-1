char nums[10][5] = {"0000","0001","0010","0011","0100","0101","0110","0111","1000","1001"};


#define joystick  A0 // Arduino pin connected to VRX pin

int xValue = 0; // To store value of the X axis

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);	// led
  pinMode(7, OUTPUT); 			// buzzer

  Serial.begin(9600);
  Serial.println("Hello. Starting system");
}

void loop()
{
  
  
  // pot
  // read analog X and Y analog values
  xValue = analogRead(joystick);

  // print data to Serial Monitor on Arduino IDE
  Serial.print("x = ");
  Serial.println(xValue);
 
 
  if(xValue>511){
    
	// upwards
    int a = 0;
    while (a < 9){
      a += 1;
      Serial.println(a);
      visu(nums[a]);
      delay(1500);
    }
   
  }else{
    
  	// downwards
    int a = 10;
  	while (a > 1){
    	a -= 1;
        Serial.println(a);
        visu(nums[a]);
      	delay(1500);
    }
 
  }
  
}

void line()
{
  digitalWrite(LED_BUILTIN, HIGH);
  tone(7, 220, 1000);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
}

void dot()
{
  digitalWrite(LED_BUILTIN, HIGH);
  tone(7, 220, 400);
  delay(400);
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
}



// n is an element of the array nums, i.e. "0001"
void visu(char *n)
{
  for (int i = 0; i < 4; i++) {
    if (n[i] == '0') {
      dot();
    } else {
      line();
    }
  }
}

