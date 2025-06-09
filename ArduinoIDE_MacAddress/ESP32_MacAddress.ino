#include "WiFi.h"

void setup() {
  Serial.begin(115200);
  
  Serial.print("MACWIfi: ");
  //Serial.println(WiFi.macAddress());
  Serial.println(Network.macAddress());
}

void loop() {

}