import platform
import psutil
import sys

print("Processors: ")
with open("/proc/cpuinfo", "r")  as f:
    info = f.readlines()

cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
for index, item in enumerate(cpuinfo):
    print("    " + str(index) + ": " + item)

# Memory
print("Memory Info: ")
with open("/proc/meminfo", "r") as f:
    lines = f.readlines()

print("     " + lines[0].strip())
print("     " + lines[1].strip())

# To Save inside file
file_path = 'log.txt'
sys.stdout = open(file_path, "w")
print("Architecture: " + platform.architecture()[0],"Machine: " + platform.machine(),"Node: " + platform.node(),"System: " + platform.system())
print("Memory Info: ")
print("     " + lines[0].strip())
print("     " + lines[1].strip())
print("Processors: ")
print("    " + str(index) + ": " + item)
print("list Of Process Names :")
for proc in psutil.process_iter(['pid', 'name', 'username']):
     print(proc.info)

