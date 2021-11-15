#include "constant.h"

int diff_10, diff_25;
unsigned long previous_loop, previous_10, previous_25, prev_time;

int SDS_25 = 0;
int SDS_10 = 0;


// I2C for BME280 sensor


ICACHE_RAM_ATTR void read_sds10()
{

  diff_10 = millis() - previous_10;
  previous_10 = millis();
  //if(diff_10<900)
  SDS_10 = diff_10;
  //digitalWrite(25, HIGH);

}

ICACHE_RAM_ATTR void read_sds25()
{
  diff_25 = millis() - previous_25;
  previous_25 = millis();
  // if(diff_25<900)
  SDS_25 = diff_25;
}

 void sds_setup()
{
  attachInterrupt(digitalPinToInterrupt(SDS25_INT), read_sds25, CHANGE);
  attachInterrupt(digitalPinToInterrupt(SDS10_INT), read_sds10, CHANGE);
  //
  //  while (!SerialMon) {
  //    ; // wait for serial port to connect. Needed for Leonardo native USB port only
  //  }
}

int sds_loop(int *SDS_2,int *SDS_1)
{
  if (millis() - prev_time > 1000)
  {

    Serial.println("");
    Serial.print("PM 2.5 is: ");*SDS_2 = SDS_25; Serial.println(SDS_25);
    Serial.print("PM 10 is: ");*SDS_1 = SDS_10; Serial.println(SDS_10);
    prev_time = millis();
  }
 // return (SDS_2);
}
