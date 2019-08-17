//https://www.arduino.cc/en/tutorial/potentiometer




int potPin = A2;    // select the input pin for the potentiometer
int ledPin = 13;   // select the pin for the LED
int val = 0;       // variable to store the value coming from the sensor

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);  // declare the ledPin as an OUTPUT
}

void loop() {
  val = analogRead(potPin);    // read the value from the sensor
  digitalWrite(LED_BUILTIN, HIGH);  // turn the ledPin on
  delay(val);                  // stop the program for some time
  digitalWrite(LED_BUILTIN, LOW);   // turn the ledPin off
  delay(val);
  Serial.println(val);
}
