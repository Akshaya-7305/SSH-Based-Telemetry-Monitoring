import time
from simulate_telemetry import get_telemetry
from ccsds_packets import build_ccsds_packet

LOG_FILE = "telemetry_packets.bin"
APID = 100
seq = 0

while True:
    data = get_telemetry()
    print("Telemetry:",data)
    packet = build_ccsds_packet(APID, seq, data)
    print("packet created")
    with open(LOG_FILE, "ab") as f:
        f.write(len(packet).to_bytes(2, "big") + packet)
        print("Packet saved")
    seq = (seq + 1) % 16384
    time.sleep(5)

