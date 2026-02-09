import nmap
import sys

# Get target and port from command line arguments or user input
if len(sys.argv) > 1:
    target = sys.argv[1]
    port = sys.argv[2] if len(sys.argv) > 2 else "80"
else:
    target = input("Enter target IP or hostname: ")
    port = input("Enter port (default 80): ") or "80"

# Create an instance of the PortScanner class
scanner = nmap.PortScanner()

# Run the scan on the target machine and port
scanner.scan(target, port)

# Get the scan results
scan_results = scanner[target]

# Print the scan results
for protocol in scan_results.all_protocols():
    print(f"Protocol: {protocol}")
    open_ports = scanner[target][protocol].keys()
    for open_port in open_ports:
        print(f"Port: {open_port} - State: {scan_results[protocol][open_port]['state']}")