// include the library code:
#include <LiquidCrystal.h>
#include "DHT.h"

// set the DHT Pin
#define DHTPIN 8

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);


int redLed = 13;
int greenLed = 10;
const int buzzer = 7;
int smokeA0 = A5;
// Your threshold value
int sensorThres = 800;


void setup() {
  // set up the LCD's number of columns and rows: 
  lcd.begin(16, 2);
  dht.begin();
  Serial.begin(9600);
  // Print a message to the LCD.
  lcd.print("Temp: Fugtighed:");

  pinMode(redLed, OUTPUT);
  pinMode(greenLed, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(smokeA0, INPUT);
}
int analogSensor;
float h;
float f;
void print();
void loop() {
  delay(500);
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  lcd.setCursor(0, 1);
  // read humidity
  h = dht.readHumidity();
  //read temperature in Fahrenheit
  f = dht.readTemperature(false);
  //Serial.println(f);

  if (isnan(h) || isnan(f)) {
    lcd.print("ERROR");
    return;
  }

  lcd.print(f);
  lcd.setCursor(7,1);
  lcd.print(h);

 print();


analogSensor = analogRead(smokeA0);

 
  // Checks if it has reached the threshold value
  if (analogSensor > sensorThres)
  {
    digitalWrite(redLed, HIGH);
    digitalWrite(greenLed, LOW);
    tone(buzzer, 1500, 4000 );
    delay(500);
    tone(buzzer, 500, 5000 );
    delay(500);
    tone(buzzer, 1500, 5000 );
    delay(500);
    tone(buzzer, 500, 5000 );
    delay(500);
    tone(buzzer, 1500, 4000 );
    delay(500);
    tone(buzzer, 500, 5000 );
    delay(500);
    tone(buzzer, 1500, 5000 );
    delay(500);
    tone(buzzer, 500, 5000 );
    delay(500);
    tone(buzzer, 1500, 5000 );
  }
  else
  {
    digitalWrite(redLed, LOW);
    digitalWrite(greenLed, HIGH);
    noTone(buzzer);
  }
  delay(100);
}
void print(){
  Serial.print(f);
  Serial.print(",");
  Serial.print(h);
  Serial.print(",");
  Serial.println(analogSensor);
  Serial.print(" ");
}




