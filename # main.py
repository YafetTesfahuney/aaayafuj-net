# main.py
from core.host_discovery import ping_sweep
from core.port_scanning import syn_scan
from core.service_detection import banner_grab

# Example usage
target = "192.168.1.1"
if ping_sweep(target):
    print(f"Host {target} is up.")
    ports = [22, 80, 443]
    for port in ports:
        if syn_scan(target, port):
            print(f"Port {port} is open.")
            banner = banner_grab(target, port)
            if banner:
                print(f"Banner: {banner}")
