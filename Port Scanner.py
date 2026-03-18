import socket
import time


target = input("Enter the target IP or website: ") # target web or ip

start_port = 1
end_port = 100

start_time = time.time()
print(f"\nScanning {target}...\n")
for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    s.close()
end_time = time.time()
total_time = end_time - start_time
print("\nScan Completed.")
print("Time taken:", round(total_time, 2), "seconds")
