from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

PACKET_LIMIT = 20
PAYLOAD_PREVIEW_BYTES = 32


def analyze_packet(packet):
    if IP not in packet:
        return

    if TCP in packet:
        protocol = "TCP"
    elif UDP in packet:
        protocol = "UDP"
    elif ICMP in packet:
        protocol = "ICMP"
    else:
        protocol = "other"

    print("-" * 40)
    print(f"Source IP: {packet[IP].src}")
    print(f"Destination IP: {packet[IP].dst}")
    print(f"Protocol: {protocol}")

    if Raw in packet:
        preview = bytes(packet[Raw].load[:PAYLOAD_PREVIEW_BYTES])
        print(f"Payload preview: {preview!r}")
    else:
        print("Payload preview: no application payload found")


print("Network Sniffer Started")
print(f"Capturing up to {PACKET_LIMIT} IP packets...")
sniff(filter="ip", prn=analyze_packet, count=PACKET_LIMIT, store=False)
print("Capture completed.")
