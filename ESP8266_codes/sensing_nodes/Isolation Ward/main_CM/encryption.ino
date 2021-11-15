#include <tinyECC.h>

tinyECC ecc;
char data[MAX_STRING_LEN];
String encry_co2;
void encry_setup()
{

}

int encry_loop(int *Co2)
{
  sprintf(data,
          "[%d, %d, %d]",
          *Co2);
  //Encryption
  ecc.plaintext = *Co2;
  Serial.println("CO2" + ecc.plaintext);
  ecc.encrypt();
  Serial.println("Cipher Text_CO2: " + ecc.ciphertext);

  encry_co2 = ecc.ciphertext ;

  
}
