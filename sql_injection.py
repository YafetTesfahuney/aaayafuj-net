# core/os_fingerprinting.py
from scapy.all import *

def os_fingerprint(target):
    response = sr1(IP(dst=target)/TCP(dport=80, flags="S"), timeout=1)
    if response:
        return response.summary()
    return None
