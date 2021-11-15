//#include <WiFiClientSecure.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

#include "constant.h"

//WiFiClientSecure httpsClient;

void connect_setup_http() {

}

bool connect_http() {

    Serial.print("HTTP Connecting: http://");
  Serial.print(CSE_IP);
  Serial.print(":");
  Serial.print(CSE_PORT);
  Serial.print("/");
  //Serial.printf("; Using finger print '%s'\n", FINGER_PRINT);
  WiFiClient client;

  // httpsClient.setFingerprint(FINGER_PRINT);
  client.setTimeout(2000);                                  // 2 Seconds
  //TODO: enable keep alive???
  delay(1000);

  int r = 0;                                                   //retry counter
  while ((!client.connect(CSE_IP, CSE_PORT)) && (r < 30)) {
      delay(1000);
      Serial.print(".");
      r++;
    }

    Serial.print("requesting URL: ");
    Serial.print(CSE_IP);

    if (r == 30) {
      Serial.print(": Connection failed");
      // return error
      return false;
    } else {
      Serial.print(": Connected to web");
      //return success
      return true;
    }
  }


  int post_request(String req) {

    Serial.print("connecting to ");
    Serial.println(CSE_IP);

    WiFiClient client;

    if (!client.connect(CSE_IP, CSE_PORT)) {
      Serial.println("connection failed to server");
      return E_OM2M_CONNECTION;
    }

    Serial.println(req + "\n");

    // Send the HTTP request
    client.print(req);

    unsigned long timeout = millis();
    while (client.available() == 0) {
      if (millis() - timeout > 5000) {
        Serial.println(">>> Client Timeout !");
        client.stop();
        return E_OM2M_NO_RESPONSE;
      }
    }
    //client = server.available();
    if (!client) {
      return E_OM2M_EMPTY_RESPONSE;
    }

    // Wait until the client sends some data
    Serial.println("reply was:");
    Serial.println("==========");
    String line;
    while (client.available()) {
      line = client.readStringUntil('\n');  //Read Line by Line
      Serial.println(line); //Print response
    }
    Serial.println("==========");
    Serial.println("closing connection");

    return SUCCESS_OM2M;
}

void disconnect_http() {
  HTTPClient http;
  Serial.print("HTTPS disconnected.");
  http.end();
}
