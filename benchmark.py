import dns.resolver
import cpuinfo
import os
import psutil
import time
from threading import Timer

start = time.time()

# function that logs benchmark every 2 seconds
def log():
    currentTime = time.time()
    if (currentTime - start) < 60:
        Timer(2, log).start()
        with open('benchmarkLogs.txt', 'a') as f:
            f.write("CPU Usage: '%s'\r\n" % str(psutil.cpu_percent()))
            f.write("Memory Usage: '%s'\r\n\n" % str(psutil.virtual_memory()))

# adds DNS server to resolv.conf
my_resolver = dns.resolver.Resolver()
my_resolver.nameservers = ['8.8.8.8']

# Display name and clockspeed of CPU
print(cpuinfo.get_cpu_info()["brand"])

# initial CPU and Memory log
with open('benchmarkLogs.txt', 'a') as f:
    f.write("Initial CPU Usage: '%s'\r\n" % str(psutil.cpu_percent()))
    f.write("Initial Memory Usage: '%s'\r\n\n" % str(psutil.virtual_memory()))
    f.close()

# run stress.ng for 60 seconds via bash command
log()
os.system("sudo stress-ng -c 1 -m 8 -t 60s")

# final CPU and Memory log
with open('benchmarkLogs.txt', 'a') as f:
    f.write("Final CPU Usage: '%s'\r\n" % str(psutil.cpu_percent()))
    f.write("Final Memory Usage: '%s'\r\n\n" % str(psutil.virtual_memory()))
    f.close()