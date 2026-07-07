import time
from read_telemetry import get_telemetry
from ccsds_packet import build_ccsds_packet

LOG_FILE = "/home/pi/telemetry_packets.bin"
APID = 100
seq = 0

while True:
    data = get_telemetry()
    packet = build_ccsds_packet(APID, seq, data)
    with open(LOG_FILE, "ab") as f:
        f.write(len(packet).to_bytes(2, "big") + packet)
    seq = (seq + 1) % 16384
    time.sleep(5)