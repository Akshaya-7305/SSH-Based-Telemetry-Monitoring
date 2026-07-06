import subprocess, json
from ccsds_packet import parse_ccsds_packet  # not strictly needed here since PC1 already parsed

PC1_IP = "203.0.113.10"
PC1_USER = "pc1_user"

def get_latest_telemetry():
    result = subprocess.run(
        ["ssh", f"{PC1_USER}@{PC1_IP}", "python3 /home/pc1/ground_station_server.py --latest"],
        capture_output=True, text=True
    )
    return result.stdout.strip()

if __name__ == "__main__":
    print("Latest satellite telemetry:")
    print(get_latest_telemetry())
