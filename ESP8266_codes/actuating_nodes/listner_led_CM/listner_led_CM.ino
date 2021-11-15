
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <Servo.h>
#include <ArduinoJson.h>
#include <tinyECC.h>

tinyECC ecc;

ESP8266WebServer server;
uint8_t pin_buzzer = D5;
const char ssid[] = "Your SSID";
const char password[] = "Your Password";

#define THRESHOLD_CO2 800
#define THRESHOLD_TEMP 70

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


  String CO2 = jObject["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:fcnt"]["CO2"];
  ecc.ciphertext = CO2;
  ecc.decrypt();
  double Co2 = ecc.plaintext.toDouble();

  String TEMP = jObject["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:fcnt"]["Temp"];
  ecc.ciphertext = TEMP;
  ecc.decrypt();
  double temp = ecc.plaintext.toDouble();


  Serial.println("test");
  if (Co2 > THRESHOLD_CO2 && temp > THRESHOLD_TEMP) {
    digitalWrite(pin_buzzer, HIGH);
    //digitalWrite(buzzer, HIGH);
    delay(300);
    digitalWrite(pin_buzzer, LOW);
    delay(300);
  }
  else {
    digitalWrite(pin_buzzer, LOW);
  }
  server.send(200, "ESP received the command");
}
