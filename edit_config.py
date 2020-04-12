# try:
# 	import pip
# except:
# 	print("PLEASE INSTALL PIP3!!!!!!!!! ---> brew reinstall python3")
# 	print("PLEASE INSTALL PIP3!!!!!!!!! ---> brew reinstall python3")
# 	print("PLEASE INSTALL PIP3!!!!!!!!! ---> brew reinstall python3")
# 	print("PLEASE INSTALL PIP3!!!!!!!!! ---> brew reinstall python3")
# 	print("PLEASE INSTALL PIP3!!!!!!!!! ---> brew reinstall python3")
# 	print("PLEASE INSTALL PIP3!!!!!!!!! ---> brew reinstall python3")
# 	print("PLEASE INSTALL PIP3!!!!!!!!! ---> brew reinstall python3")
# 	input()
import sys

from threading import *
import time
import math
import os

def ossT(msg):
	os.system(msg)
	print("############################")
	print("############################")
	print("############################")
	print(msg)
	print("############################")
	print("############################")
	print("############################")

def oss(msg):
	t = Thread(target = ossT, args = [msg,])
	t.start()

def install(package):
	oss("python3 -m pip install "+package)
	# pip.main(['install', package])


try:
	import pyautogui
except ImportError:
	install('pyautogui')
	import pyautogui



try:
	import yaml
except ImportError:
	install('pyyaml')
import yaml

import io
# TV configuration
# tv_config = {
# "tv":
#   {"host": "192.168.43.144",
#   "protocol": "wss",
#   "port": 8002},
# "controller": {
#   "name": "RoozRemote"}
#   }

path = 'config.yml'
# Write YAML file
# with io.open(path, 'w+', encoding='utf8') as outfile:
# 	yaml.dump(tv_config, outfile, default_flow_style=False, allow_unicode=True)

# Read YAML file
configuration = None
with open(path, 'r') as stream:
	data_loaded = yaml.safe_load(stream)
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print(data_loaded)
	configuration = data_loaded

try:

	if configuration is not None and "tv" in configuration:
		tv_ip = configuration["tv"]["host"]
		tv_port = configuration["tv"]["port"]
		# protocol = configuration["tv"]["protocol"]
except:
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	print("error loading config", path)
	tv_ip = "0.0.0.0"
	tv_port = 8002
# protocol = "wss"

a = pyautogui.prompt(text='Please update your ip! check your tv settings', title='TV IP ADDRESS CONFIG' , default=tv_ip)
print("!!!!!",a)
p = 8002
tv_ip = a
if ":" in a:
	tv_ip = a.split(":")[0]
	pa = a.split(":")[1]
	try:
		p = int(pa)
	except:
		p = 8002
tv_port = p

print(tv_ip, tv_port)

configuration["tv"]["host"] = tv_ip
configuration["tv"]["port"] = tv_port

# Write YAML file
with io.open(path, 'w+', encoding='utf8') as outfile:
	yaml.dump(configuration, outfile, default_flow_style=False, allow_unicode=True)

with open(path, 'r') as stream:
	data_loaded = yaml.safe_load(stream)
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print(data_loaded)
	configuration = data_loaded

print("!!!!!!!!!!!!!!")
print(configuration)
