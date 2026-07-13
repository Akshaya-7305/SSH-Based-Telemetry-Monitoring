import sys
from ccsds_packet import parse_ccsds_packet

LOG_FILE = "telemetry_packets.bin"

def read_all_packets():
    packets = []
    with open(LOG_FILE, "rb") as f:
        data = f.read()
    i = 0
    while i < len(data):
        pkt_len = int.from_bytes(data[i:i+2], "big")
        raw = data[i+2:i+2+pkt_len]
        try:
            packets.append(parse_ccsds_packet(raw))
        except ValueError as e:
            print(f"Rejected packet at offset {i}: {e}", file=sys.stderr)
        i += 2 + pkt_len
    return packets

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--latest":
        pkts = read_all_packets()
        print(pkts[-1] if pkts else "No telemetry yet")
    else:
        for p in read_all_packets():
            print(p)