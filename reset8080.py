import subprocess
import os
from threading import Thread
import time

def ossT(msg):
	os.system(msg)
	# print("############################")
	# print("############################")
	print("############################")
	print(msg)
	print("############################")
	# print("############################")
	# print("############################")

def oss(msg):
	t = Thread(target = ossT, args = [msg,])
	t.start()

# print("@@@@@@@@@@@")
proc = ""
try:
	proc = subprocess.check_output("lsof -i:8080", shell=True);
except:
	pass
# print("@@@@@@@@@@@")
if len(str(proc).split("\\n"))>=2:
	# print("@@@@@@@@@@@")
	line = str(proc).split("\\n")[1]
	while("  " in line):
		line = line.replace("  "," ")

	line = line.split(" ")
	print(line)
	if "python" in line[0].lower() or "sams" in line[0].lower():
		oss("kill "+line[1])
		# xproc = subprocess.check_output("kill "+line[1], shell=True);
		print("CLOSED PREVIOUS PROC",line[1],":::::::::::")#,xproc)
		time.sleep(1)

# print("@@@@@@@@@@@#")
