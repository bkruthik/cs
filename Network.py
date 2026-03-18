import psutil
import time
import matplotlib.pyplot as plt

upload = [];download = []
print("Network Traffic Monitor Started")

# get starting network data
old = psutil.net_io_counters()

for i in range(20):   
    time.sleep(1)     

    new = psutil.net_io_counters()

    up = (new.bytes_sent - old.bytes_sent) / 1024
    down = (new.bytes_recv - old.bytes_recv) / 1024

    upload.append(up)
    download.append(down)

    print("Upload:", round(up,2), "KB/s",
          "| Download:", round(down,2), "KB/s")

    old = new
#Graph
plt.plot(upload)
plt.plot(download)
plt.title("Network Traffic Visualizer")
plt.xlabel("Time")
plt.ylabel("Speed KB/s")
plt.legend(["Upload", "Download"])
plt.show()
