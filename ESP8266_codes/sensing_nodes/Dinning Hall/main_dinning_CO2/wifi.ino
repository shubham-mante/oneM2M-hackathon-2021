#include <ESP8266WiFi.h>
#include "constant.h"

void wifi_setup()
{
 WiFi.begin(WIFI_SSID, WIFI_PASS);

  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println();

  Serial.print("Connected, IP address: ");
  Serial.println(WiFi.localIP());
  digitalWrite(LED, HIGH);
}


void wifi_loop()
{
  
}
