import subprocess

# Replace these with the actual values at ISRO
PC1_USER = "your_username"
PC1_HOST = "your_hostname_or_ip"

REMOTE_COMMAND = "python ground_station_server.py --latest"

def get_latest_telemetry():
    try:
        result = subprocess.run(
            ["ssh", f"{PC1_USER}@{PC1_HOST}", REMOTE_COMMAND],
            capture_output=True,
            text=True,
            check=True
        )

        print("\n========== Latest Telemetry ==========\n")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print("SSH command failed.")
        print(e.stderr)

    except FileNotFoundError:
        print("SSH client not found. Please install OpenSSH.")

if __name__ == "__main__":
    get_latest_telemetry()
