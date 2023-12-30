import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.stderr.decode('utf-8')

def main():
    while True:
        print("1. Run Nmap Scan")
        print("2. Run Nikto Scan")
        print("3. Run Performance Test")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            ip = input("Enter IP address: ")
            port = input("Enter port (optional): ")
            result = run_command(f"nmap {ip} {port}")
            print(result)

        elif choice == '2':
            url = input("Enter URL: ")
            result = run_command(f"nikto -h {url}")
            print(result)

        elif choice == '3':
            # Add performance testing command
            pass

        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

