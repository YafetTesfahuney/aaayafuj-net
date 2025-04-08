# core/service_detection.py
import socket

def banner_grab(target, port):
    s = socket.socket()
    s.settimeout(2)
    try:
        s.connect((target, port))
        banner = s.recv(1024)
        return banner.decode().strip()
    except Exception as e:
        return None
