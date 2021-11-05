/*------------------------------------------------------------------------------
  11/01/2016
  Author: Makerbro
  Platforms: ESP8266
  Language: C++/Arduino
  File: webserver_rx_json.ino
  ------------------------------------------------------------------------------
  Description: 
  Code for YouTube video demonstrating how to send JSON-formatted data to a 
  webserver running on an ESP8266.
  https://youtu.be/Edbxyl2BhyU
  Do you like my videos? You can support the channel:
  https://patreon.com/acrobotic
  https://paypal.me/acrobotic
  ------------------------------------------------------------------------------
  Please consider buying products from ACROBOTIC to help fund future
  Open-Source projects like this! We'll always put our best effort in every
  project, and release all our design files and code for you to use. 
  https://acrobotic.com/
  https://amazon.com/acrobotic
  ------------------------------------------------------------------------------
  License:
  Please see attached LICENSE.txt file for details.
------------------------------------------------------------------------------*/
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <Servo.h>
#include <ArduinoJson.h>

ESP8266WebServer server;
uint8_t pin_led = D3;
char* ssid = "GalaxyM21";
char* password = "agtp5971";

Servo servo_pan;
Servo servo_tilt;

void setup()
{
  servo_pan.attach(D1);
  servo_tilt.attach(D2);
  pinMode(pin_led, OUTPUT);
  WiFi.begin(ssid,password);
  Serial.begin(115200);
  while(WiFi.status()!=WL_CONNECTED)
  {
    Serial.print(".");
    delay(500);
  }
  Serial.println("");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  server.on("/",[](){server.send(200,"text/plain","Hello World!");});
  server.on("/toggle",toggleLED);
  server.begin();
}

void loop()
{
  server.handleClient();
}

void toggleLED()
{
  String data = server.arg("plain");
  StaticJsonBuffer<500> jBuffer;
  JsonObject& jObject = jBuffer.parseObject(data);
  double pm25 = jObject["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:fcnt"]["PM25"];
  Serial.println("test");
  if(pm25 > 40.0){
  digitalWrite(pin_led, HIGH);
  }
  else{
  digitalWrite(pin_led, LOW);
  }
  server.send(200,"ESP received the command");
}
