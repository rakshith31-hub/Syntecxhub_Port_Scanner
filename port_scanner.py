import socket
import threading
import datetime

print("\n===== SYNTECXHUB TCP PORT SCANNER =====\n")

target = input("Enter target IP or hostname: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

# Log file
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"scan_log_{timestamp}.txt"


def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN]   Port {port}")
            with open(log_file, "a") as f:
                f.write(f"OPEN   Port {port}\n")
        else:
            with open(log_file, "a") as f:
                f.write(f"CLOSED Port {port}\n")

        s.close()

    except Exception as e:
        with open(log_file, "a") as f:
            f.write(f"ERROR Port {port}: {str(e)}\n")


threads = []

print("\nScanning...\n")

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("\nScan completed!")
print(f"Log saved to {log_file}")
