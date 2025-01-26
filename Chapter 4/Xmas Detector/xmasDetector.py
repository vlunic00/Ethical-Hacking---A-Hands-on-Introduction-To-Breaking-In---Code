from scapy.all import *

def scan_flags(packet):

	suspicious_flags = "FPU"

	if packet.haslayer(TCP):
		if packet['TCP'].flags == "FPU":
			print(f"Xmas Attack Detected - Attacker IP: {packet['IP'].src}")



if __name__ == "__main__":
	capture = sniff(prn=scan_flags)
