/*
  Copywrite Gabriel Schippa 2022.  All rights reserved
  File Name: ADCwithSerialOutput.ino
  Project Name: Raspberry Pi Oscilloscope with Fourier Analysis Capability
*/

#include <Wire.h>

//Make a counter to be incremented by 1.
uint16_t counter = 0;

//Define an input pin
const int SIGNAL_INPUT_PIN = 3;

//Define a variable to hold the value recieved from the input pin
int input;

void setup() {
  //Setup Serial port:
  Serial.begin(38400);

  //Setup pin Input (Not Needed Yet)
  pinMode(SIGNAL_INPUT_PIN, INPUT_PULLUP);

  //Make it so that the arduino with sample at a faster rate:
  ADCSRA = (ADCSRA & 0xf8) | 0x04;

  /*
  //While waiting for the other device to respond, send a capital A every 300 milliseconds
  while(!Serial.available())
  {
    Serial.write('A');
    delay(300);
  }
  */
  
}

void loop() {

  //This section of code will be for sending the analog signal to the pi
  input = analogRead(SIGNAL_INPUT_PIN);
  Serial.println(input);
  
  /*
  Serial.println(counter);
  
  //Iterate the binary counter
  if(counter < 1024)
    counter++;
   else
    counter = 0;
   */
}
