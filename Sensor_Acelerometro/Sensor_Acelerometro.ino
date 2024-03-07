#include <ESP8266WiFi.h>
#include <Wire.h>
#include <MPU6050_tockn.h>

const char* ssid = "Amarildo";
const char* password = "a2s4f7d22";
const char* host = "192.168.1.104";
const int port = 80;

MPU6050 mpu6050(Wire);

WiFiClient client;

void setup() {
  Serial.begin(115200);
  Wire.begin();
  mpu6050.begin();

  Serial.println("Conectando ao WiFi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Tentando se conectar ao WiFi...");
  }

  Serial.println("Conectado ao WiFi com sucesso!");
}

void loop() {
  mpu6050.update();

  float x = mpu6050.getAccX();
  float y = mpu6050.getAccY();
  float z = mpu6050.getAccZ();

  if (client.connect(host, port)) {
    Serial.println("Conectado ao servidor");

    client.print("POST /save_data HTTP/1.1\r\n");
    client.print("Host: ");
    client.print(host);
    client.print("\r\n");
    client.print("Content-Type: application/json\r\n");
    client.print("Content-Length: ");
    client.print(30); 
    client.print("\r\n\r\n");

    String data = "";
    data += String(x, 2); 
    data += ",";
    data += String(y, 2);
    data += ",";
    data += String(z, 2);

    client.print(data);

    delay(1000);

    client.stop();
    Serial.println("Dados enviados com sucesso!");
  } else {
    Serial.println("Falha ao conectar ao servidor");
  }

  delay(1000);
}