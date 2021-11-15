
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <Servo.h>
#include <ArduinoJson.h>
#include <tinyECC.h>

tinyECC ecc;

ESP8266WebServer server;
uint8_t pin_led = D3;
const int buzzer =  D5;
const char ssid[] = "Your SSID";
const char password[] = "Your Password";

#define THRESHOLD_CO2 800

Servo servo_pan;
Servo servo_tilt;

void setup()
{
  servo_pan.attach(D1);
  servo_tilt.attach(D2);
  pinMode(pin_led, OUTPUT);
  WiFi.begin(ssid, password);
  Serial.begin(115200);
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(500);
  }
  Serial.println("");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  server.on("/", []() {
    server.send(200, "text/plain", "Hello World!");
  });
  server.on("/toggle", toggleLED);
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

  String PM25 = jObject["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:fcnt"]["PM25"];
  ecc.ciphertext = PM25;
  ecc.decrypt();
  double pm25 = ecc.plaintext.toDouble();

  String PM10 = jObject["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:fcnt"]["PM10"];
  ecc.ciphertext = PM10;
  ecc.decrypt();
  double pm10 = ecc.plaintext.toDouble();

  String CO2 = jObject["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:fcnt"]["CO2"];
  ecc.ciphertext = CO2;
  ecc.decrypt();
  double Co2 = ecc.plaintext.toDouble();



Co2= 900;
  Serial.println("test");
  if (Co2 > THRESHOLD_CO2) {
    digitalWrite(pin_led, HIGH);
    //digitalWrite(buzzer, HIGH);
    delay(300);
    digitalWrite(pin_led, LOW);
    delay(300);
  }
  else {
    digitalWrite(pin_led, LOW);
  }
  server.send(200, "ESP received the command");
}
