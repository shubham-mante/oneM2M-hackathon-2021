#include <tinyECC.h>

tinyECC ecc;
char data[MAX_STRING_LEN];
String encry_PM10, encry_PM25, encry_co2, encry_temp, encry_hum;
void encry_setup()
{

}

int encry_loop(int *Co2, int *pm25, int *pm10, int *temp, int *hum)
{
  sprintf(data,
          "[%d, %d, %d]",
          *Co2, *pm25, *pm10);
  //Encryption
  ecc.plaintext = *Co2;
  Serial.println("CO2" + ecc.plaintext);
  ecc.encrypt();
  Serial.println("Cipher Text_CO2: " + ecc.ciphertext);

  encry_co2 = ecc.ciphertext ;

  ecc.plaintext = *pm25;
  Serial.println("PM2.5" + ecc.plaintext);
  ecc.encrypt();
  Serial.println("Cipher Text_PM25: " + ecc.ciphertext);

  encry_PM25 = ecc.ciphertext ;

  ecc.plaintext = *pm10;
  Serial.println("PM10" + ecc.plaintext);
  ecc.encrypt();
  Serial.println("Cipher Text_PM10: " + ecc.ciphertext);
  encry_PM10 = ecc.ciphertext ;


  ecc.plaintext = *temp;
  Serial.println("Temp" + ecc.plaintext);
  ecc.encrypt();
  Serial.println("Cipher Text_Temp: " + ecc.ciphertext);

  encry_temp = ecc.ciphertext ;


  ecc.plaintext = *hum;
  Serial.println("Hum" + ecc.plaintext);
  ecc.encrypt();
  Serial.println("Cipher Text_Hum: " + ecc.ciphertext);

  encry_hum = ecc.ciphertext ;

}
