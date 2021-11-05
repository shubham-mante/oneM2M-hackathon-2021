#include <ESP8266WiFi.h>

const char* ssid = "GalaxyM21";
const char* password = "agtp5971";
const char* host = "192.168.162.234"; //it will tell you the IP once it starts up
//just write it here afterwards and upload
int ledPin = D3;


WiFiServer server(3000); //just pick any port number you like

void setup() {
  Serial.begin(115200);
  delay(10);
  Serial.println(WiFi.localIP());
  // prepare GPIO2
  pinMode(ledPin, OUTPUT);
  digitalWrite(D3, LOW);

  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");

  // Start the server
  server.begin();
  Serial.println("Server started");

  // Print the IP address
  Serial.println(WiFi.localIP());
}

void loop() {
  // Check if a client has connected

  WiFiClient client = server.available();
  if (!client) {
    return;
  }

  // Wait until the client sends some data
  while (!client.available()) {
    delay(1);
  }

  // Read the first line of the request
  String req = client.readStringUntil('\r');
  client.flush();

  // Match the request
  if (req.indexOf("") != -10) {  //checks if you're on the main page

    if (req.indexOf("/OFF") != -1) { //checks if you clicked OFF
      digitalWrite(ledPin, LOW);
      Serial.println("You clicked OFF");
    }
    if (req.indexOf("/ON") != -1) { //checks if you clicked ON
      digitalWrite(ledPin, HIGH);
      Serial.println("You clicked ON");
    }
  }

  else {
    Serial.println("invalid request");
    client.stop();
    return;
  }

  // Prepare the response
  String s = "HTTP/1.1 200 OK\r\n";
  s += "Content-Type: application/json\r\n\r\n";
  s += "{"
        "\"status\": \"Command Successfully Received by ESP8266\","
         "}";

  client.flush();


  // Send the response to the client
  client.print(s);
  delay(1);



}
