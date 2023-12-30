import nmap

# Replace {{target}} with the IP address or hostname of the target machine
target = "192.168.2.8"
# Replace {{port}} with the port number you want to scan
port = "1234"

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