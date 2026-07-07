import struct, hmac, hashlib, json, time

SECRET_KEY = b"replace_this_with_a_strong_shared_secret_32bytes"  # same on Pi, PC1, PC2

def build_ccsds_packet(apid, seq_count, payload_dict):
    payload = json.dumps(payload_dict).encode()
    pkt_len = len(payload) - 1

    version_type_sec = (0 << 13) | (0 << 12) | (0 << 11) | (apid & 0x7FF)
    seq_flags_count = (0b11 << 14) | (seq_count & 0x3FFF)

    primary_header = struct.pack(">HHH", version_type_sec, seq_flags_count, pkt_len)
    packet_body = primary_header + payload

    digest = hmac.new(SECRET_KEY, packet_body, hashlib.sha256).digest()
    return packet_body + digest  # HMAC appended at the end

def parse_ccsds_packet(raw):
    body, digest = raw[:-32], raw[-32:]
    expected = hmac.new(SECRET_KEY, body, hashlib.sha256).digest()
    if not hmac.compare_digest(digest, expected):
        raise ValueError("HMAC verification failed — packet rejected")

    version_type_sec, seq_flags_count, pkt_len = struct.unpack(">HHH", body[:6])
    apid = version_type_sec & 0x7FF
    seq_count = seq_flags_count & 0x3FFF
    payload = json.loads(body[6:].decode())
    return {"apid": apid, "seq_count": seq_count, "payload": payload}