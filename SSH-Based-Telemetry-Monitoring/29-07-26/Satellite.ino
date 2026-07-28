const int LED_PIN = 8;

void setup() {
    pinMode(LED_PIN, OUTPUT);
    digitalWrite(LED_PIN, LOW);

    Serial.begin(9600);
}

void loop() {

    if (Serial.available() > 0) {

        String command = Serial.readStringUntil('\n');
        command.trim();

        // Flash once when an SSH command is detected
        if (command == "ACTIVITY") {

            digitalWrite(LED_PIN, HIGH);
            delay(300);

            digitalWrite(LED_PIN, LOW);

            Serial.println("ACTIVITY_OK");
        }

        // Blink 5 times for the actual BLINK telecommand
        else if (command == "BLINK") {

            for (int i = 0; i < 5; i++) {

                digitalWrite(LED_PIN, HIGH);
                delay(500);

                digitalWrite(LED_PIN, LOW);
                delay(500);
            }

            Serial.println("SUCCESS");
        }

        else if (command == "ON") {

            digitalWrite(LED_PIN, HIGH);
            Serial.println("LED_ON");
        }

        else if (command == "OFF") {

            digitalWrite(LED_PIN, LOW);
            Serial.println("LED_OFF");
        }
    }
}