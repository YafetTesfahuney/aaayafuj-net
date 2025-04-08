# main.py
from utils import load_config
from network_tools import check_ports, scan_network

def main():
    config = load_config()
    scan_network(config)
    check_ports(config)

if __name__ == "__main__":
    main()
