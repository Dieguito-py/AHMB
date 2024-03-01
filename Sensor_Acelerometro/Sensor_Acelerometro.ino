#include <ESP8266WiFi.h>
#include <Wire.h>

const char* ssid = "Amarildo";
const char* password = "a2s4f7d22";
const char* serverAddress = "192.168.1.104";
const int serverPort = 8080;

const int MPU6050_ADDRESS = 0x68;

const float ACCEL_MIN = -2.0;
const float ACCEL_MAX = 2.0;

void setup() {
  Serial.begin(115200);
  Wire.begin();
  Wire.write(0x6B); // Endereço do registrador para controle de energia
  Wire.write(0x00); 
  // Conectar-se à rede WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando ao WiFi...");
  }
  Serial.println("Conectado ao WiFi");

  delay(1000);
}

void loop() {
  // Ler dados do MPU6050
  int16_t accelerometerData[3];
  readMPU6050Data(accelerometerData);

  // Mapear os valores do acelerômetro para o intervalo desejado
  float x_mapped = mapFloat(accelerometerData[0], -32768, 32767, ACCEL_MIN, ACCEL_MAX);
  float y_mapped = mapFloat(accelerometerData[1], -32768, 32767, ACCEL_MIN, ACCEL_MAX);
  float z_mapped = mapFloat(accelerometerData[2], -32768, 32767, ACCEL_MIN, ACCEL_MAX);

  // Enviar dados para o servidor Python
  sendDataToServer(x_mapped, y_mapped, z_mapped);

  delay(1000);  // Ajuste o intervalo conforme necessário
}

void readMPU6050Data(int16_t* data) {
  Wire.beginTransmission(MPU6050_ADDRESS);
  Wire.write(0x3B);  // Endereço do registrador inicial do acelerômetro
  Wire.endTransmission(false);
  Wire.requestFrom(MPU6050_ADDRESS, 6, true);

  for (int i = 0; i < 3; i++) {
    data[i] = Wire.read() << 8 | Wire.read();
  }
}

void sendDataToServer(float x, float y, float z) {
  // Criar uma instância do cliente WiFi
  WiFiClient client;
  
  // Conectar-se ao servidor Python
  if (client.connect(serverAddress, serverPort)) {
    // Montar a string com os dados
    String dataString = String(x, 2) + "," + String(y, 2) + "," + String(z, 2);

    // Enviar a string para o servidor
    client.print("POST /receber_dados HTTP/1.1\r\n");
    client.print("Host: ");
    client.print(serverAddress);
    client.print("\r\n");
    client.print("Content-Type: application/x-www-form-urlencoded\r\n");
    client.print("Content-Length: ");
    client.print(dataString.length());
    client.print("\r\n\r\n");
    client.print(dataString);

    Serial.println("\n Dados enviados para o servidor");
    Serial.print(dataString);
    // Aguardar a resposta do servidor (opcional)
    while (client.available()) {
      String line = client.readStringUntil('\r');
      Serial.print(line);
    }

    // Fechar a conexão com o servidor
    client.stop();
  } else {
    Serial.println("Falha ao conectar-se ao servidor");
  }
}

float mapFloat(float x, float in_min, float in_max, float out_min, float out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
