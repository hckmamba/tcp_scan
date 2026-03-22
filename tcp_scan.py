import socket
import sys

input_host = input("Enter the target host (IP or domain): ")
if not input_host:
    print("No host provided. Exiting.")
    sys.exit(1)

def scan_port(host, port, timeout=1):
    """
    Attempt to connect to a port on the target host.
    Returns True if the port is open, False otherwise.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        return False

def tcp_scan(host, ports, timeout=1):
    """
    Scan multiple ports on the target host.
    """
    open_ports = []
    print(f"\nStarting TCP scan on {host}...")
    print(f"Scanning {len(ports)} ports...\n")
    
    for port in ports:
        if scan_port(host, port, timeout):
            open_ports.append(port)
            print(f"Port {port}: OPEN")
    
    print(f"\n--- Scan Results ---")
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found.")
    
    return open_ports

if __name__ == "__main__":
    host = input_host.strip()
    
    # Common ports to scan
    common_ports = [
        20, 21,      # FTP
        22,          # SSH
        23,          # Telnet
        25,          # SMTP
        53,          # DNS
        80,          # HTTP
        110,         # POP3
        143,         # IMAP
        443,         # HTTPS
        445,         # SMB
        8080, 8443,  # Common web ports
        3306,        # MySQL
        5432,        # PostgreSQL
        6379,        # Redis
        27017,       # MongoDB
    ]
    
    # Optional: Scan a range of ports
    ports = range(1, 1025)  # Scan ports 1-1024
    
    tcp_scan(host, common_ports, timeout=1)
