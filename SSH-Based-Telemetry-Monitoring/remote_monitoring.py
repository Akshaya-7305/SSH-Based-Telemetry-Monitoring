import subprocess

# Replace these with the actual values at ISRO
PC1_HOST = "GROUND-PC1"      # Example: GROUND-PC1 or 192.168.1.20
PC1_USER = "student"         # Example: student

def get_latest_telemetry():
    try:
        result = subprocess.run(
            [
                "ssh",
                f"{PC1_USER}@{PC1_HOST}",
                "python ground_station_server.py --latest"
            ],
            capture_output=True,
            text=True,
            check=True
        )

        print("========== Latest Satellite Telemetry ==========")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print("SSH connection failed!")
        print(e.stderr)

    except FileNotFoundError:
        print("SSH client not found. Install OpenSSH Client on Windows.")

if __name__ == "__main__":
    get_latest_telemetry()