import subprocess
import json

# ==============================
# PC1 SSH Configuration
# ==============================

PC1_IP = "192.168.1.100"          # Replace with the IP address of PC1
PC1_USER = "pc1_user"             # Replace with the username of PC1
REMOTE_SCRIPT = "/home/pc1/ground_station_server.py"

# ==============================
# Function to fetch telemetry
# ==============================

def get_latest_telemetry():
    """
    Connects to PC1 using SSH and fetches the latest telemetry packet.
    """

    command = [
        "ssh",
        f"{PC1_USER}@{PC1_IP}",
        f"python3 {REMOTE_SCRIPT} --latest"
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        telemetry = json.loads(result.stdout)

        return telemetry

    except subprocess.CalledProcessError as e:
        print("SSH Connection Failed")
        print(e.stderr)
        return None

    except json.JSONDecodeError:
        print("Received invalid telemetry data.")
        print(result.stdout)
        return None


# ==============================
# Main Program
# ==============================

def main():

    telemetry = get_latest_telemetry()

    if telemetry is None:
        return

    print("\n========== Latest Satellite Telemetry ==========\n")

    print(f"Timestamp      : {telemetry.get('timestamp')}")
    print(f"Temperature    : {telemetry.get('temperature_C')} °C")
    print(f"Humidity       : {telemetry.get('humidity_percent')} %")

    print(f"Acceleration X : {telemetry.get('accel_x')}")
    print(f"Acceleration Y : {telemetry.get('accel_y')}")
    print(f"Acceleration Z : {telemetry.get('accel_z')}")

    print(f"Gyroscope X    : {telemetry.get('gyro_x')}")
    print(f"Gyroscope Y    : {telemetry.get('gyro_y')}")
    print(f"Gyroscope Z    : {telemetry.get('gyro_z')}")

    print("\n===============================================\n")


if __name__ == "__main__":
    main()
