from scapy.all import sniff, IP, TCP, UDP, ICMP
def analyze_packet(packet):
    if IP in packet:
        source = packet[IP].src
        destination = packet[IP].dst
        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"
        else:
            protocol = "other"
        print("-" * 40)
        print(f"Source IP:{source}")
        print(f"Destination IP: {destination}")
        print(f"Protocol:  {protocol}")


print("Network Sniffer Started")
print("Capturing 20 packets...")
sniff(filter="ip", prn=analyze_packet, count=20, store=False)
print("capture completed!")

