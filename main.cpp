#include <Arduino.h>
#include <WiFi.h>
#include <esp_now.h>
#include <esp_sleep.h>
#include <esp_wifi.h>

#define VRx 36 // Analog pin for X
#define VRy 39 // Analog pin for Y

#define DELAY 10

// Variables
uint8_t mac_address[] = {0x40, 0x22, 0xD8, 0xF0, 0xE0, 0xA0};

// Setup LED ring

typedef struct
{
  int coordinate;
} esp_message;

// Function declarations
esp_message getGridMapping(int, int);
void onDataRecv(const uint8_t *, const uint8_t *, int);
void onDataSent(const uint8_t *, esp_now_send_status_t);


void setup()
{
  setCpuFrequencyMhz(80);
  
  Serial.begin(115200);
  while (!Serial);

  WiFi.mode(WIFI_STA);

  Serial.println();

  // Set up the ESP-NOW
  if (esp_now_init() != ESP_OK)
  {
    Serial.println("Error initializing ESP-NOW");
    return;
  }

  // Replace the peer setup section with this:
  esp_now_peer_info_t peerInfo = {};
  memcpy(peerInfo.peer_addr, mac_address, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;

  if (esp_now_add_peer(&peerInfo) != ESP_OK)
  {
    Serial.println("Failed to add peer");
    return;
  }

  esp_now_register_recv_cb(onDataRecv);
  esp_now_register_send_cb(onDataSent);

  // Reduce wifi power consumption
  esp_wifi_set_max_tx_power(8);

  // Set up light sleep
  esp_sleep_enable_timer_wakeup(150000 - DELAY * 1000); // 150 ms
  Serial.println("Setup done");
}

int AVG_WINDOW = 1;
int last_msg = 0;
void loop()
{

  // Read from adc
  int x_sum = 0;
  int y_sum = 0;
  for (int i = 0; i < AVG_WINDOW; i++)
  {
    x_sum += analogRead(VRx);
    y_sum += analogRead(VRy);
  }
  int x = x_sum / AVG_WINDOW;
  int y = y_sum / AVG_WINDOW;
  // Check if x and y are outside the specified range
  if (x < 1365 || x > 2730 || y < 1365 || y > 2730)
  {
    // wake up wifi
    esp_wifi_start();
    esp_now_init();

    esp_message msg = getGridMapping(x, y);
    last_msg = msg.coordinate;
    Serial.print("(");
    Serial.print(x);
    Serial.print(", ");
    Serial.println(y);
    Serial.print(") | Mapped to grid: ");
    Serial.println(msg.coordinate);
    
    // Broadcast the message
    esp_now_send(mac_address, (uint8_t *)&msg, sizeof(msg));
  } else {
    if (last_msg != 5) {
      last_msg = 5;
      Serial.println("Center");
      Serial.println();
      Serial.print("Last msg:");
      Serial.println(last_msg);
      esp_message msg;
      msg.coordinate = 5;
      esp_wifi_start();
      esp_now_init();
      esp_now_send(mac_address, (uint8_t *)&msg, sizeof(msg));
    }
  }


  delay(DELAY);
  esp_wifi_stop();
  esp_light_sleep_start();
}

esp_message getGridMapping(int x, int y)
{
  int x1 = 1365, x2 = 2730;
  int y1 = 1365, y2 = 2730;

  int col = (x < x1) ? 0 : (x < x2) ? 1 : 2;
  int row = (y < y1) ? 0 : (y < y2) ? 1 : 2;

  esp_message msg;
  msg.coordinate = (row * 3) + col + 1;
  
  return msg;
}

// Receive Callback
void onDataRecv(const uint8_t *mac, const uint8_t *incomingData, int len)
{
  esp_message msg;
  memcpy(&msg, incomingData, sizeof(msg));
  Serial.print("Received coordinate: ");
  Serial.println(msg.coordinate);
}

// Send Callback
void onDataSent(const uint8_t *mac, esp_now_send_status_t status)
{
  Serial.print("Last Packet Send Status: ");
  if (status == ESP_NOW_SEND_SUCCESS)
  {
    Serial.println("Delivery Success");
  }
  else
  {
    Serial.println("Delivery Fail");
  }
}
