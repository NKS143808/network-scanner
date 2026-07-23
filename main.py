from scapy.all import ARP, Ether, srp

print("=" * 40)
print("     NETWORK SCANNER")
print("=" * 40)

target = input("Enter Network Range (Example: 192.168.1.0/24): ")

arp = ARP(pdst=target)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")

packet = ether / arp

result = srp(packet, timeout=2, verbose=False)[0]

print("\nActive Devices")
print("-" * 40)

for sent, received in result:
    print(f"IP Address : {received.psrc}")
    print(f"MAC Address: {received.hwsrc}")
    print("-" * 40)
