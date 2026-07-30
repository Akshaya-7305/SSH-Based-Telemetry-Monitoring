const byte LED_PIN = 8;

void setup()
{
    pinMode(LED_PIN, OUTPUT);
    digitalWrite(LED_PIN, LOW);

    Serial.begin(9600);

    Serial.println("SATELLITE READY");
}

void loop()
{
    if (Serial.available() > 0)
    {
        String command = Serial.readStringUntil('\n');
        command.trim();

        // SSH command activity -> flash once
        if (command.equalsIgnoreCase("ACTIVITY"))
        {
            digitalWrite(LED_PIN, HIGH);
            delay(300);
            digitalWrite(LED_PIN, LOW);

            Serial.println("ACTIVITY_OK");
        }

        // Actual remote BLINK command -> blink 5 times
        else if (command.equalsIgnoreCase("BLINK"))
        {
            for (int i = 0; i < 5; i++)
            {
                digitalWrite(LED_PIN, HIGH);
                delay(500);

                digitalWrite(LED_PIN, LOW);
                delay(500);
            }

            Serial.println("SUCCESS");
        }

        // Keep LED ON
        else if (command.equalsIgnoreCase("ON"))
        {
            digitalWrite(LED_PIN, HIGH);

            Serial.println("LED_ON");
        }

        // Turn LED OFF
        else if (command.equalsIgnoreCase("OFF"))
        {
            digitalWrite(LED_PIN, LOW);

            Serial.println("LED_OFF");
        }

        // Unknown command
        else
        {
            Serial.print("UNKNOWN COMMAND: ");
            Serial.println(command);
        }
    }
}