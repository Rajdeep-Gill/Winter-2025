#include <Arduino.h>
#include "WiFi.h"
#include <Adafruit_NeoPixel.h>
#include <esp_now.h>

#define LED_OUTPUT_PIN 16
#define NUMPIXELS 12
#define DELAYVAL 2000

Adafruit_NeoPixel pixels(NUMPIXELS, LED_OUTPUT_PIN, NEO_GRB + NEO_KHZ800);

uint8_t receiverAddress[] = {0x40, 0x22, 0xD8, 0xF0, 0xE0, 0xA0};

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
  Serial.print("Last Packet Send Status: ");
  if (status == ESP_NOW_SEND_SUCCESS) {
    Serial.println("Delivery Success");
  } else {
    Serial.println("Delivery Fail");
  }
}

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_MODE_STA);
  Serial.println(WiFi.macAddress());

  pixels.begin();
  pixels.clear();
  
  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }

  // Register send callback
  esp_now_register_send_cb(OnDataSent);
  
  // Register peer
  esp_now_peer_info_t peerInfo = {};
  memcpy(peerInfo.peer_addr, receiverAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;
  
  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    Serial.println("Failed to add peer");
    return;
  }
  Serial.println("ESP-NOW Sender Setup Complete");

}

int WINDOW_SIZE = 8;

// Directions:
// 1: bottom left
// 2: bottom
// 3: bottom right
// 4: left
// 5: middle
// 6: right
// 7: Top left
// 8: Top
// 9: Top right

void turnLedOn(int direction){

  switch (direction)
  {
    case 1:
      pixels.setPixelColor(1, pixels.Color(0, 150, 0));
      pixels.setPixelColor(2, pixels.Color(0, 150, 0));
      break;
    case 2:
      pixels.setPixelColor(0, pixels.Color(0, 150, 0));
      break;
    case 3:
      pixels.setPixelColor(10, pixels.Color(0, 150, 0));
      pixels.setPixelColor(11, pixels.Color(0, 150, 0));
      break;
    case 4:
      pixels.setPixelColor(3, pixels.Color(0, 150, 0));
    case 5:
      // middle - do nothing
      break;
    case 6:
      pixels.setPixelColor(9, pixels.Color(0, 150, 0));
      break;
    case 7:
      pixels.setPixelColor(4, pixels.Color(0, 150, 0));
      pixels.setPixelColor(5, pixels.Color(0, 150, 0));
      break;
    case 8:
      pixels.setPixelColor(6, pixels.Color(0, 150, 0));
      break;
    case 9:
      pixels.setPixelColor(7, pixels.Color(0, 150, 0));
      pixels.setPixelColor(8, pixels.Color(0, 150, 0));
      break;
    default:
      break;
  }

}


void loop() {

  pixels.clear();

  int xTotal = 0;
  for (int i = 0; i < WINDOW_SIZE; i++){
    xTotal += analogRead(39);
  }
  int xVal = xTotal/WINDOW_SIZE;
  // Serial.print("X Value: ");
  // Serial.println(xTotal);

  int yTotal = 0;
  for (int i = 0; i < WINDOW_SIZE; i++){
    yTotal += analogRead(36);
  }
  int yVal = yTotal/WINDOW_SIZE;

  // Serial.print("Y Value: ");
  // Serial.println(yVal);

  // Serial.print("(");
  // Serial.print(xVal);
  // Serial.print(", ");
  // Serial.print(yVal);
  // Serial.println(")");

  // Check if its up or down
  int dirCode = 5; // middle
  if (xVal < 2000 && xTotal > 1700) {
    if (yVal < 100) {
      dirCode = 8;
      Serial.println("UP!");
      // pixels.setPixelColor(6, pixels.Color(0, 150, 0));
    } else if (yVal > 3800) {
      Serial.println("DOWN!");
      dirCode = 2;
      // pixels.setPixelColor(0, pixels.Color(0, 150, 0));
    }
  }

  // Check if its left or right
  if (yVal < 1900 && yVal > 1700) {
    if (xVal < 100) {
      dirCode = 4;
      Serial.println("LEFT!");
      // pixels.setPixelColor(3, pixels.Color(0, 150, 0));
    } else if (xVal > 3900) {
      dirCode = 6;
      Serial.println("RIGHT!");
      // pixels.setPixelColor(9, pixels.Color(0, 150, 0));
    }
  }

  // Top Left
  if (xVal < 10 && yVal < 10) {
    Serial.println("TOP LEFT!");
    dirCode = 7;
    // pixels.setPixelColor(4, pixels.Color(0, 150, 0));
    // pixels.setPixelColor(5, pixels.Color(0, 150, 0));
  }

  // Top Right
  if (xVal > 4000 && yVal < 10) {
    Serial.println("TOP RIGHT");
    dirCode = 9;
    // pixels.setPixelColor(7, pixels.Color(0, 150, 0));
    // pixels.setPixelColor(8, pixels.Color(0, 150, 0));
  }

  // Bottom Left
  if (xVal < 10 && yVal > 4000) {
    Serial.println("BOTTOM LEFT!");
    dirCode = 1;
    // pixels.setPixelColor(1, pixels.Color(0, 150, 0));
    // pixels.setPixelColor(2, pixels.Color(0, 150, 0));
  }

  // Bottom Right
    if (xVal > 4000 && yVal > 4000) {
    Serial.println("BOTTOM RIGHT");
    dirCode = 3;
    // pixels.setPixelColor(10, pixels.Color(0, 150, 0));
    // pixels.setPixelColor(11, pixels.Color(0, 150, 0));
  }


  turnLedOn(dirCode);
  pixels.show();

  esp_now_send(receiverAddress, (uint8_t *)&dirCode, sizeof(dirCode));

  // Serial.println("---------------");
  // Send data every 300ms
  delay(300);
}

