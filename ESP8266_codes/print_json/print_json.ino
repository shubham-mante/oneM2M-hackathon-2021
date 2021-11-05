#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ArduinoJson.h>




const char* ssid = "GalaxyM21";
const char* password = "agtp5971";
char c;
String readString = String(100);
WiFiServer wifiServer(80);


void setup() {

  Serial.begin(9600);
  delay(1000);

  WiFi.begin(ssid, password);
  WiFi.mode(WIFI_STA);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting..");
  }

  Serial.print("Connected to WiFi. IP:");
  Serial.println(WiFi.localIP());
  wifiServer.begin();

}


//for parsing the actual JSON later  
//you can ignore this at this moment because I don't even get the needed string to parse it from JSON
void handleReceivedMessage(String message){

  StaticJsonBuffer<500> JSONBuffer;                     //Memory pool
  JsonObject& parsed = JSONBuffer.parseObject(message); //Parse message

  if (!parsed.success()) {   //Check for errors in parsing

    Serial.println("Parsing failed");
    return;

  }

  const char * name3 = parsed["m2m:sgn"];           //Get name from HTTP
  Serial.println("name3");
}


void loop() {
  WiFiClient client = wifiServer.available();


  if (client) {
  Serial.println("Client connected");


    while (client.connected()) {

      while (client.available()>0) {
        //instream from mobipale device

        char c = client.read();
        if (readString.length() < 100) {

         //store characters to string
         readString.concat(c);
         //Serial.print(c);
}
      //Serial.print(c);
//if HTTP request has ended
       if (c == '\n') {
          //Serial.println(readString);   
          delay(50);  
          //handleReceivedMessage(readString);         
          readString = "";
          client.stop();
   }
 }}}}
