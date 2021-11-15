#include <SoftwareSerial.h>
#include <MHZ.h>
#include "constant.h"

int ppm_pwm;

MHZ co2(MH_Z19_RX, MH_Z19_TX, CO2_IN, MHZ14A);

void co2_setup() {
  pinMode(CO2_IN, INPUT);
  delay(100);
  Serial.println("MHZ 14A");

  // enable debug to get addition information
  // co2.setDebug(true);

//  if (co2.isPreHeating()) {
//    Serial.print("Preheating");
//    while (co2.isPreHeating()) {
//      Serial.print(".");
//      delay(5000);
//    }
//    Serial.println();
//  }
}

void co2_loop(int *ppm_pwm) {
  Serial.print("\n----- Time from start: ");
  Serial.print(millis() / 1000);
  Serial.println(" s");
  *ppm_pwm = co2.readCO2PWM();
  Serial.print(", PPMpwm: ");
  Serial.print(*ppm_pwm);

  Serial.println("\n------------------------------");
  delay(5000);
}
