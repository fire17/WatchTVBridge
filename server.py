
import socket
import sys

from threading import *
import time
import math
import os

def ossT(msg):
	os.system(msg)
	print("############################")
	print("############################")
	print(msg)
	print("############################")
	print("############################")

def oss(msg):
	t = Thread(target = ossT, args = [msg,])
	t.start()

def install(package):
	oss("python3 -m pip install "+package)

try:
	import pyautogui
except ImportError:
	install('pyautogui')
	import pyautogui

try:
	import pynput
except ImportError:
	install('pynput')
	import pynput

from pynput.mouse import Button, Controller

from subprocess import call


withVolume = False
sendHomeOnStart = True
starterX, starterY = [None], [None]

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

print(tv_ip, tv_port)

# input()

pc_def = False

targetmode = "tv"
# curl = "curl -X POST http://localhost:8080/key/"
# tv_ip = '10.0.0.9'
# tv_port = 8001
readback = True

reconnecting = False

print()
print("TV_IP:",tv_ip, tv_port)
print()
from samsungtv_server.controllers import SamsungTV
def send(key, rep = 1):
	global targetmode
	if "tv" in targetmode:
		for a in range(rep):
			t = Thread(target = post_key, args = [key,])
			t.start()

# tv = SamsungTV(tv_ip, tv_port, read = readback)
tv = None
tv_connected = False

def initTV(data = None):
	global tv, tv_ip, reconnecting, tv_connected
	if reconnecting is False:
		reconnecting = True
		if tv is not None:
			tv.connection.close()
		tv = SamsungTV(tv_ip, tv_port, read = readback)
		reconnecting = False
		tv_connected = True
		print()
		print("  #####################################")
		print("  #####################################")
		print("  ###       YOUR TV IS READY!       ###")
		print("  ############# MAGICHO_TV ############")
		print("  #####################################")
		print("  #####################################")
		print()

ti = Thread(target = initTV, args = [None,])
ti.start()

print()
print("trying to connect to tv..",tv_ip,tv_port)

timeout = 3
tvi = time.time()
while(time.time()-tvi<timeout and not tv_connected):
	pass

if tv_connected:
	targetmode = "tv"
else:
	targetmode = "pc"

if pc_def:
	targetmode = "pc"




def post_key(key, r = 0):  # noqa: E501

	global tv, reconnecting
	"""post_key

	Sends a remote control key to the TV # noqa: E501

	:param key:
	:type key: str

	:rtype: None
	"""
	if not reconnecting:
		key = key.upper()
		if (key.find('KEY_') != 0):
			key = 'KEY_' + key
		try:
			tv.send_key(key, 1)
		except Exception as err:
			tv.logger.error("................")
			tv.logger.error('2______Could not send the key. Error: {}'.format(err))
			if r == 0:
				tv.logger.error("................")
				tv.logger.error("trying again....")
				tv.logger.error("reconnecting....")
				tv.logger.error("................")
				tv.connection.close()
				initTV()
				post_key(key,r+1)
			else:
				tv.logger.error("................")
				tv.logger.error("FAILED>>>>>>....")
				tv.logger.error("................")
				tv.logger.error("................")








import logging
# import socket

# log = logging.getLogger('udp_server')

import logging
import subprocess

log = logging.getLogger('udp_server')


def udp_server(host='0.0.0.0', port=9093):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		try:
			print("@@@@@@@@@@@")
			proc = subprocess.check_output("lsof -i:8080", shell=True);
			print("@@@@@@@@@@@")
			if len(str(proc).split("\\n"))>=2:
				print("@@@@@@@@@@@")
				line = str(proc).split("\\n")[1]
				while("  " in line):
					line = line.replace("  "," ")
				line = line.split(" ")
				if "python" in line[0].lower():
					xproc = subprocess.check_output("kill "+line[1], shell=True);
					print("CLOSED PREVIOUS PROC",line[1],":::::::::::")#,xproc)
					time.sleep(1)
			print("@@@@@@@@@@@#")

		except:
			print("@@@@@@@@@@@!")
			pass
		log.info("Listening on udp %s:%s" % (host, port))




		# print("::::::::::::::::::::::::::::::::::::")
		# print(":::::::::::: MAGICHO_TV ::::::::::::")
		# print("::::::::::::::::::::::::::::::::::::")

		s.bind((host, port))
		while True:
				(data, addr) = s.recvfrom(128*124)
				yield data


# FORMAT_CONS = '%(asctime)s %(name)-12s %(levelname)8s\t%(message)s'
# logging.basicConfig(level=logging.DEBUG, format=FORMAT_CONS)
#
# for data in udp_server():
# 		log.debug("%r" % (data,))


# FORMAT_CONS = '%(asctime)s %(name)-12s %(levelname)8s\t%(message)s'
# logging.basicConfig(level=logging.DEBUG, format=FORMAT_CONS)


# SEND:::
# import socket
# msg = "Hello, World!"
# byte_message = bytes(msg, "utf-8")
# opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# opened_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# opened_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# while(True):
# opened_socket.sendto(byte_message, ("255.255.255.255", 9093))


# Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

'''
# Bind the socket to the address given on the command line
server_name = socket.gethostbyname(socket.gethostname())

# server_name = "172.20.10.7" # OR enter ip manually (disable ' ' ' comment) michael's
# server_name = "192.168.43.86" # OR enter ip manually (disable ' ' ' comment) lichay's

server_address = (server_name, 9999)
print("######################## MOFO Right hand")
print("########################")
print("########################")

print ('starting up on %s port %s' % server_address)
# sock.settimeout(1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_address)
sock.listen(1)
'''

# pyautogui.moveTo(100, 150)
curX, curY = pyautogui.position()
lastPosition = pyautogui.position()
readySteady = [True]
steadyxy = [0,0]
lastData = time.time()+10

action = [""]
actionP = ["xxx"]
maxSum = 0

pyautogui.FAILSAFE = False
lastAction = None
lastActionTime = time.time()
mouse = Controller()
canMove = [True]

# pyautogui.moveTo(0,0)
holder = [None]
tx = time.time()
def m(data):
	a,b = data
	pyautogui.moveTo(a,b)
	# print("moved to ",a,b)

# def getTo(to, fro):
#     global holder
#     tox, toy = to[0]+0, to[1]+0
#     fromx, fromy = fro[0]+0, fro[1]+0
#
#     mtime = time.time()
#     holder[0] = mtime
#
#     dx = tox-fromx
#     dy = toy-fromy
#
#     if dx <= 1 or dy <= 1:
#         pyautogui.moveTo(tox,toy)
#         return True
#
#     dmax = dx
#     if dy> dmax:
#         dmax = dy
#     dmax = int(math.sqrt(dmax))
#
#     xstep = int((dx-1)/dmax)
#     ystep = int((dy-1)/dmax)
#     count = 0
#     for a in range(dmax):
#         count+=1
#         txa = Thread(target = m, args = [[fromx+count*xstep,fromy+count*ystep],])
#         time.sleep(0.01)
#         txa.start()
#         if holder[0] is not mtime:
#             return True
#     txa = Thread(target = m, args = [[tox,toy],])
#     time.sleep(0.01)
#     txa.start()
		# print(a)
# print("took",time.time()-tx)
# magic.test.watchkit.extension
# com.magicho.watchtvalpha.watchkit.extension



boxesSizeX = 250
boxesSizeY = 250
currBoxX = -1
currBoxY = -1

def delay(data):
	time.sleep(data[0])
	print("moving",data)
	global curX, curY
	curX, curY = data[1]

def getCloser(at):
	# atx, aty = pyautogui.position()
	t1 = Thread(target = delay, args=[[3,[200,500]],])
	t1.start()

	t2 = Thread(target = delay, args=[[6,[300,300]],])
	t2.start()

	atx, aty = at
	if atx is None or aty is None:
		atx, aty = pyautogui.position()

	global curX, curY, canMove
	# toX = None
	# toY = None
	while True:



		if (atx != curX or aty != curY) and canMove[0]:
			dx, dy = curX - atx, curY - aty
			if abs(dx) <= 1 or abs(dy) <= 1:
				m([curX,curY])
				atx, aty = curX, curY
				print("got here")
			else:
				dmax = abs(dx)
				# tempiX, tempiY = 1, 1
				if abs(dy)> dmax:
					dmax = abs(dy)

				# if dy < 0:
				#     tempiY *= -1
				# if dx < 0:
				#     tempiX *= -1

				# print(dmax)
				dmax = int(math.sqrt(abs(dmax)))


				xstep = int((dx-1)/dmax)
				ystep = int((dy-1)/dmax)

				if abs(xstep) < 1:
					if xstep <0:
						xstep = -1
					else:
						xstep = 1

				if abs(ystep) < 1:
					if ystep <0:
						ystep = -1
					else:
						ystep = 1

				toX = atx + xstep
				toY = aty + ystep

				txa = Thread(target = m, args = [[toX,toY],])
				txa.start()
				atx, aty = toX, toY
				# time.sleep(0.01)

	# time.sleep(0.001)
	# getCloser([toX, toY])

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

from pynput.keyboard import Key, Controller
keyboard = Controller()

def volume(times = 1, by = 6):
	global keyboard
	key = None
	if times is 0:
		key = Key.media_volume_mute
	elif times > 0:
		key = Key.media_volume_up
	else:
		key = Key.media_volume_down
	if key is not None:
		for a in range(int(abs(times))):
			keyboard.press(key)
			keyboard.release(key)

# volume(-3)
	# vol = subprocess.check_output("osascript -e 'output volume of (get volume settings)'", shell=True);
	# vol = int(str(vol).split("'")[1].split('\\')[0])
	# vol += times*by
	# call(["osascript -e 'set volume output volume "+str(vol)+"'"], shell=True)



# def toggleTarget(data):
# 	global targetmode
# 	time.sleep(1)
# 	failed = False
# 	while(True and not failed):
# 		print()
# 		if "tv" in targetmode.lower():
# 			print("  #####################################")
# 			print("  ###          TARGET = TV          ###")
# 			print("  #####################################")
# 			print()
# 			print("  IP/PORT: ",tv_ip, tv_port)
# 			print()
# 			print("  Press Enter to toggle between TV/PC mode")
# 			print()
# 			print()
# 		else:
# 			print()
# 			print("  #####################################")
# 			print("  ###          TARGET = PC          ###")
# 			print("  #####################################")
# 			print()
# 			print("  Press Enter to toggle between TV/PC mode")
# 			print()
# 			print()
# 		try:
# 			tmode = input()
# 			if "1" in tmode.lower() or "t" in tmode.lower():
# 				targetmode = "tv"
# 			elif "2" in tmode.lower() or "p" in tmode.lower() or "m" in tmode.lower():
# 				targetmode = "pc"
# 			else:
# 				print()
# 				print(" PLEASE ENTER:")
# 				print("   1 or t: TV mode")
# 				print("   2 or p: PC mode")
# 				print()
#
#
# 			### TOGGLE
# 			# if "tv" in targetmode.lower():
# 			# 	targetmode = "pc"
# 			# else:
# 			# 	targetmode = "tv"
# 		except:
# 			failed = True
# 			pass
#
# ttt = Thread(target = toggleTarget, args = [None,])
# ttt.start()

rt = [time.time()+10]
rtMax = 1
resetNext = True

# def stableMouse(data):
# 	global rt, rtMax, resetNext, starterX, starterY
# 	# global targetmode
# 	# time.sleep(1)
# 	failed = False
# 	# rt = time.time()
# 	# while(True and not failed):
# 	# 	try:
# 	# 		if time-time()-rt>rtMax:
# 	# 			# starterX[0], starterY[0] = None, None
# 	# 			resetNext = True
# 	# 	except:
# 	# 		failed = True
# 	# 		pass
#
# tttr = Thread(target = stableMouse, args = [None,])
# tttr.start()


xoffset, yoffset = [0],[0]

def getScreenRes():
	#get actual screen res
	return pyautogui.size()
	return 1960,1080

resW, resH = getScreenRes()

boxX, boxY = None, None
boxR = 170


def moveMouse(data):
	global maxSum, action, actionP, curX, curY, lastAction, lastActionTime, mouse, canMove
	global currBoxX, currBoxY, boxesSizeX, boxesSizeY, targetmode
	global xoffset, yoffset, resH, resW, resetNext, withVolume, rt
	global boxX, boxY, boxR
	print("starting moveMouse")
	firstTemp = True
	tempX, tempY = -1,-1
	t = time.time()
	mt = time.time()
	keydict = {"x-1":"left", "x1":"right","y-1":"down", "y1":"up"}
	lastPr = [""]
	while(True):
		if targetmode is not "pc":
			time.sleep(1)
		else:
			if time.time()-mt > 3:
				maxSum = 0
				mt = time.time()
			if action[0] not in ["","m","n","\'"] and action[0] not in lastPr:
				lastPr[0] = action[0]
				for aa in range(10):
					aaa = str(action[0])
					for ba in range(5):
						aaa+= aaa
					# print(aaa)
				# print()
			if action[0] == "m":
				rt[0] = time.time()
				lastAction = "move"
				lastActionTime = time.time()

				if boxX is None or boxY is None:
					boxX, boxY = curX, curY

				boxDist = math.sqrt(pow(curX-boxX,2)+pow(curY-boxY,2))
				if boxDist > boxR and canMove[0]:
					gox, goy = curX-boxX, (curY-boxY)*-1
					xkey,ykey = "x", "y"
					if gox <0:
						xkey += "-"
					if goy <0:
						ykey += "-"
					xkey+="1"
					ykey+="1"
					keys = [xkey, ykey]
					chosenKey = 0
					if abs(goy)>abs(gox):
						chosenKey = 1

					for a in range(int(1*boxDist/boxR)):
						send(keydict[keys[chosenKey]])

					boxX, boxY = curX, curY

				# toBoxX = int(curX/boxesSizeX)
				# toBoxY = int(curY/boxesSizeY)
				# # print()
				# # print()
				# # print(toBoxX,toBoxY)
				# # print()
				# if (toBoxX != currBoxX or toBoxY != currBoxX) and canMove[0]:
				# 	if currBoxX is -1 or currBoxY is -1:
				# 		currBoxX, currBoxY = toBoxX, toBoxY
				# 	else:
				# 		dict = {"x-1":"left", "x1":"right","y-1":"down", "y1":"up"}
				# 		gox, goy = toBoxX - currBoxX, currBoxY - toBoxY
				# 		xkey,ykey = "x", "y"
				# 		if gox <0:
				# 			xkey += "-"
				# 		if goy <0:
				# 			ykey += "-"
				# 		xkey+="1"
				# 		ykey+="1"
				#
				#
				# 		for a in range(abs(gox)):
				# 			# msg = curl+dict[xkey]
				# 			send(dict[xkey])
				# 			# t = Thread(target = oss, args = [msg,])
				# 			# t.start()
				# 			# oss(msg)
				# 			# os.system(curl+dict[xkey])
				# 		for a in range(abs(goy)):
				# 			# msg = curl+dict[ykey]
				# 			send(dict[ykey])
				# 			# print("############################")
				# 			# print(msg)
				# 			# print("############################")
				# 			# oss(msg)
				#
				# 			# os.system(curl+dict[ykey])
				#
				# 		currBoxX = toBoxX
				# 		currBoxY = toBoxY

				if tempX != curX or tempY != curY:
					# getTo([curX,curY],[tempX,tempY])

					# if resetNext:
					# 	# resetNext = True
					# 	tempX,tempY = pyautogui.position()
					# 	firstTemp = False
					# diffx, diffy = curX-tempX, curY-tempY
					#
					# if resetNext:
					# 	xoffset-=diffx
					# 	yoffset-=diffy

					tempX,tempY = curX, curY

					# if tempX < 0 :
					# 	xoffset[0] = 0 - tempX
					# if tempY < 0 :
					# 	yoffset[0] = 0 - tempY
					#
					# if tempX > resW :
					# 	xoffset[0] = resW - tempX
					# if tempY > resH :
					# 	yoffset[0] = resH - tempY

					if tempX + xoffset[0] < 0 :
						xoffset[0] = 0 - tempX
					if tempY + yoffset[0] < 0 :
						yoffset[0] = 0 - tempY

					if tempX + xoffset[0] > resW :
						xoffset[0] = resW - tempX
					if tempY + yoffset[0] > resH :
						yoffset[0] = resH - tempY





					resetNext = False
					# resetNext


					if targetmode is "pc":
						pyautogui.moveTo(tempX+xoffset[0],tempY+yoffset[0])
						print("MMMMMMMMMMMMMMMMMMM")
						print(tempX+xoffset[0],tempY+yoffset[0])
						print("MMMMMMMMMMMMMMMMMMM")


					canMove[0] = True
					t = time.time()
					# actionP[0] = action[0]
			if action[0] == "n":
				resetNext = True

			if action[0] == "b":

				if lastAction != "back" or time.time()-lastActionTime>0.8:
					print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
					# print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
					# print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
					# print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
					# print()
					send("return")

					# pyautogui.click(clicks=1)
					canMove[0] = False

					if targetmode is "pc":
						pyautogui.keyDown('ctrl')  # hold down the shift key
						pyautogui.press('left')     # press the left arrow key
						pyautogui.keyUp('ctrl')
					# mouse.click(Button.left)
					# actionP[0] = action[0]
				else:
					print("AFTER back")
					print()
					canMove[0] = False
				lastAction = "back"
				lastActionTime = time.time()
				action[0] = "n"

			if action[0] == "f":
				if lastAction != "front" or time.time()-lastActionTime>0.8:
					print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
					# print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
					# print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
					# print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
					# print()
					send("return")

					# pyautogui.click(clicks=1)
					canMove[0] = False

					if targetmode is "pc":
						pyautogui.keyDown('ctrl')  # hold down the shift key
						pyautogui.press('right')     # press the left arrow key
						pyautogui.keyUp('ctrl')
					# mouse.click(Button.left)
					# actionP[0] = action[0]
				else:
					print("AFTER front")
					print()
					canMove[0] = False
				lastAction = "front"
				lastActionTime = time.time()
				action[0] = "n"

			if action[0] == "h":

				if lastAction != "home" or time.time()-lastActionTime>0.8:
					print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
					# print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
					# print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
					# print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
					# print()
					send("home")

					# pyautogui.click(clicks=1)
					canMove[0] = False

					if targetmode is "pc":
						pyautogui.keyDown('ctrl')  # hold down the shift key
						pyautogui.press('up')     # press the left arrow key
						pyautogui.keyUp('ctrl')
					# mouse.click(Button.left)
					# actionP[0] = action[0]
				else:
					print("AFTER home")
					print()
					canMove[0] = False
				lastAction = "home"
				lastActionTime = time.time()
				action[0] = "n"

			if action[0] == "v"  and withVolume:
				rt[0] = time.time()
				if lastAction != "volup" or time.time()-lastActionTime>0.001:
					print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
					# print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
					# print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
					# print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
					# print()
					send("volup")

					if targetmode is "pc":
						# pyautogui.keyDown('ctrl')  # hold down the shift key
						pyautogui.press('volumeup')     # press the left arrow key
						volume(1)
						# call(["osascript -e 'set volume output volume 100'"], shell=True)
						# pyautogui.keyUp('ctrl')
					# pyautogui.click(clicks=1)
					canMove[0] = False
					# mouse.click(Button.left)
					# actionP[0] = action[0]
				else:
					print("AFTER volup")
					print()
					canMove[0] = False
				lastAction = "volup"
				lastActionTime = time.time()
				action[0] = "n"

			if action[0] == "w" and withVolume:
				rt[0] = time.time()
				if lastAction != "voldown" or time.time()-lastActionTime>0.001:
					print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
					# print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
					# print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
					# print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
					# print()
					send("voldown")

					if targetmode is "pc":
						# pyautogui.keyDown('ctrl')  # hold down the shift key
						volume(-1)
						# pyautogui.press('volumedown')     # press the left arrow key
						# pyautogui.keyUp('ctrl')

					# pyautogui.click(clicks=1)
					canMove[0] = False
					# mouse.click(Button.left)
					# actionP[0] = action[0]
				else:
					print("AFTER voldown")
					print()
					canMove[0] = False
				lastAction = "voldown"
				lastActionTime = time.time()
				action[0] = "n"

			if action[0] == "c":
				# print(time.time()-lastActionTime,"***********************")
				if lastAction != "click" or time.time()-lastActionTime>0.8:
					print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
					# print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
					# print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
					# print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
					# print()
					send("enter")

					# pyautogui.click(clicks=1)
					canMove[0] = False
					if targetmode is "pc":
						mouse.click(Button.left)
					lastActionTime = time.time()
					lastAction = "click"
					# actionP[0] = action[0]
				else:

					# print("AFTER CLICK")
					# print()
					canMove[0] = False
				action[0] = "n"

			if time.time()-t > 3:
				if data[0] is not None:
					try:
						data[0].close()
						pass
					except:
						pass
				t = time.time()

con = [None]
t = Thread(target = moveMouse, args = [con,])
t.start()

tg = Thread(target = getCloser, args = [[None,None],])
# tg.start()

if sendHomeOnStart:
	print("SXSCKSJXNCISCJOSJCOSJCOJSOCJ")
	print("SXSCKSJXNCISCJOSJCOSJCOJSOCJ")
	print("SXSCKSJXNCISCJOSJCOSJCOJSOCJ")
	send("home")

def setStarters(data):
	global starterX, starterY
	x,y = data
	px, py = pyautogui.position()
	starterX[0], starterY[0] = px-x, py-y
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@",starterX, starterY , px, py)
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")



stableCount = 0
stableMaxTime = 0.8

def stableMouse(at):
	global lastData, lastPosition, readySteady, steadyxy
	while(True):
		if time.time()-lastData > 1:

			lastPosition = pyautogui.position()
			readySteady[0] = True
			lastData = time.time()

		time.sleep(0.01)

tg = Thread(target = stableMouse, args = [[None,None],])
tg.start()

pcmousekey = "AAA"

watchlock = True

def printKey(key):
	if "up" in key.lower():
		print("  _   _               ")
		print(" | | | |  _ __        ")
		print(" | | | | | '_ \\       ")
		print(" | |_| | | |_) |      ")
		print("  \\___/  | .__/       ")
		print("         |_|          ")
		print("")
	if "down" in key.lower():
		print("  ____                               ")
		print(" |  _ \\    ___   __      __  _ __    ")
		print(" | | | |  / _ \\  \\ \\ /\\ / / | '_ \\   ")
		print(" | |_| | | (_) |  \\ V  V /  | | | |  ")
		print(" |____/   \\___/    \\_/\\_/   |_| |_|  ")
		print("")
	if "left" in key.lower():
		print("  _               __   _   ")
		print(" | |       ___   / _| | |_ ")
		print(" | |      / _ \\ | |_  | __|")
		print(" | |___  |  __/ |  _| | |_ ")
		print(" |_____|  \\___| |_|    \\__|")
		print("")
	if "right" in key.lower():
		print("  ____    _           _       _   ")
		print(" |  _ \\  (_)   __ _  | |__   | |_ ")
		print(" | |_) | | |  / _` | | '_ \\  | __|")
		print(" |  _ <  | | | (_| | | | | | | |_ ")
		print(" |_| \\_\\ |_|  \\__, | |_| |_|  \\__|")
		print("              |___/               ")
		print(" ")
	if "click" in key.lower():
		print("   ____   _       ___    ____   _  __  _ ")
		print("  / ___| | |     |_ _|  / ___| | |/ / | |")
		print(" | |     | |      | |  | |     | ' /  | |")
		print(" | |___  | |___   | |  | |___  | . \\  |_|")
		print("  \\____| |_____| |___|  \\____| |_|\\_\\ (_)")
		print("                                         ")
		print(" ")
	if "home" in key.lower():
		print("  _   _    ___    __  __   _____   _ ")
		print(" | | | |  / _ \\  |  \\/  | | ____| | |")
		print(" | |_| | | | | | | |\\/| | |  _|   | |")
		print(" |  _  | | |_| | | |  | | | |___  |_|")
		print(" |_| |_|  \\___/  |_|  |_| |_____| (_)")
		print(" ")
	if "back" in key.lower():
		print("  ____       _       ____   _  __  _ ")
		print(" | __ )     / \\     / ___| | |/ / | |")
		print(" |  _ \\    / _ \\   | |     | ' /  | |")
		print(" | |_) |  / ___ \\  | |___  | . \\  |_|")
		print(" |____/  /_/   \\_\\  \\____| |_|\\_\\ (_)")
		print(" ")
	if "front" in key.lower():
		print("  _____   ____     ___    _   _   _____   _ ")
		print(" |  ___| |  _ \\   / _ \\  | \\ | | |_   _| | |")
		print(" | |_    | |_) | | | | | |  \\| |   | |   | |")
		print(" |  _|   |  _ <  | |_| | | |\\  |   | |   |_|")
		print(" |_|     |_| \\_\\  \\___/  |_| \\_|   |_|   (_)")
		print(" ")
	if "volume" in key.lower():
		print(" __     __          _     _   _         ")
		print(" \\ \\   / /   ___   | |   | | | |  _ __  ")
		print("  \\ \\ / /   / _ \\  | |   | | | | | '_ \\ ")
		print("   \\ V /   | (_) | | |   | |_| | | |_) |")
		print("    \\_/     \\___/  |_|    \\___/  | .__/ ")
		print("                                 |_|    ")
		print(" ")
	if "wolume" in key.lower():
		print(" __     __          _     ____                             ")
		print(" \\ \\   / /   ___   | |   |  _ \\    ___   __      __  _ __  ")
		print("  \\ \\ / /   / _ \\  | |   | | | |  / _ \\  \\ \\ /\\ / / | '_ \\ ")
		print("   \\ V /   | (_) | | |   | |_| | | (_) |  \\ V  V /  | | | |")
		print("    \\_/     \\___/  |_|   |____/   \\___/    \\_/\\_/   |_| |_|")
		print("                                                           ")
		print("")
	if "unlock" in key.lower():
		print("  _   _           _                  _                 _ ")
		print(" | | | |  _ __   | |   ___     ___  | | __   ___    __| |")
		print(" | | | | | '_ \\  | |  / _ \\   / __| | |/ /  / _ \\  / _` |")
		print(" | |_| | | | | | | | | (_) | | (__  |   <  |  __/ | (_| |")
		print("  \\___/  |_| |_| |_|  \\___/   \\___| |_|\\_\\  \\___|  \\__,_|")
		print("                                                         ")
		print("")
	elif "lock" in key.lower():
		print("   _                      _                 _ ")
		print("  | |       ___     ___  | | __   ___    __| |")
		print("  | |      / _ \\   / __| | |/ /  / _ \\  / _` |")
		print("  | |___  | (_) | | (__  |   <  |  __/ | (_| |")
		print("  |_____|  \\___/   \\___| |_|\\_\\  \\___|  \\__,_|")
		print("")




def printNumberToBigStr(num, a = "", b = "", c = "", d = "", e = ""):
	A = ["  ___   ","   _    "," ____   "," _____  "," _  _   "," ____   ","  __    "," _____  ","  ___   ","  ___   "]
	B = [" / _ \\  ","  / |   ","|___ \\  ","|___ /  ","| || |  ","| ___|  "," / /_   ","|___  | "," ( _ )  "," / _ \\  "]
	C = ["| | | | ","  | |   ","  __) | ","  |_ \\  ","| || |_ ","|___ \\  ","| '_ \\  ","   / /  "," / _ \\  ","| (_) | "]
	D = ["| |_| | ","  | |   "," / __/  "," ___) | ","|__   _|"," ___) | ","| (_) | ","  / /   ","| (_) | "," \\__, | "]
	E = [" \\___/  ","  |_|   ","|_____| ","|____/  ","   |_|  ","|____/  "," \\___/  "," /_/    "," \\___/  ","   /_/  "]


	for x in [a,b,c,d,e]:
		x+= "            "
	for charrrr in str(num):
		a+=A[int(charrrr)]
		b+=B[int(charrrr)]
		c+=C[int(charrrr)]
		d+=D[int(charrrr)]
		e+=E[int(charrrr)]

	print(a)
	print(b)
	print(c)
	print(d)
	print(e)

datacounter = -1

def dash():
	global watchlock, lastAction
	print()
	print()
	print()
	print()
	print()
	print()
	print()
	if not watchlock:
		print(" _   _   _   _   _        ___     ____   _  __  _____   ____  ")
		print("| | | | | \\ | | | |      / _ \\   / ___| | |/ / | ____| |  _ \\ ")
		print("| | | | |  \\| | | |     | | | | | |     | ' /  |  _|   | | | |")
		print("| |_| | | |\\  | | |___  | |_| | | |___  | . \\  | |___  | |_| |")
		print(" \\___/  |_| \\_| |_____|  \\___/   \\____| |_|\\_\\ |_____| |____/ ")
	else:
		print(" _        ___     ____   _  __  _____   ____  ")
		print("| |      / _ \\   / ___| | |/ / | ____| |  _ \\ ")
		print("| |     | | | | | |     | ' /  |  _|   | | | |")
		print("| |___  | |_| | | |___  | . \\  | |___  | |_| |")
		print("|_____|  \\___/   \\____| |_|\\_\\ |_____| |____/ ")
	print()
	print("LAST ACTION: ",lastAction)
	printKey(lastAction)
	printNumberToBigStr(datacounter)












for data in udp_server():
	# global starterY, starterX
		# log.debug("%r" % (data,))

	try:#if True: #try:
		if pcmousekey in str(data):
			print(":::::::INCOMING:::::::")
			print(data)
			print("::::::::::::::::::::::")
			targetmode = "pc"
			msg = str(data).split("b\'")[-1]
			action[0] = msg.split("AAA")[-1].split("ZZZ")[0]
			angles = msg.split("ZZZ")[-1].split("FFF")[0].split(":")
			asum = float(msg.split("___")[-1].split("AAA")[0].split("\'")[0])
			print("aaaa")
			x, y = msg.split("___")[0].split("@")[-1].split(",")
			print("bbbbb")
			x = int(x)
			y = int(y)

			# if starterX[0] is None or starterY[0] is None or time.time()-rt[0]>0.8:
			# 	rt[0] = time.time()
			# 	rtt = Thread(target = setStarters, args = [[x,y],])
			# 	rtt.start()
			if action[0] is "m":
				lastData = time.time()

			if readySteady[0]:
				print(lastPosition)
				steadyxy = [(lastPosition.x - x)-xoffset[0], (lastPosition.y - y)-yoffset[0]]
				# steadyxy = [lastPosition.x - x, lastPosition.y - y]

				# xoffset[0], yoffset[0] = 0, 0
				stableCount += 1
				if stableCount is 1:
					stableTime = time.time()

				if stableCount > 1:
				# if time.time()-stableTime > stableMaxTime
					readySteady[0] = False
			else:
				stableCount = 0

			curX, curY = x+steadyxy[0],y+steadyxy[1]
			if asum> maxSum:
				maxSum = asum
				# print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
				# print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
				# print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

			print("GOT DATA:")
			print("(X,Y):  ",x,",",y)
			print("ACCEL:  ",asum)
			print("MAXSUM: ",maxSum)
			print("ACTION: ",action)
		else:
			targetmode = "tv"
			msg = str(data).split("b\'")[-1].split('\'')[0]
			tvaction = msg.split("#")[0]

			print("MMMM",msg)
			datacounter = int(msg.split("#")[-1])
			print("!!!!!!!!",datacounter)

			if "right" in tvaction.lower():
				print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM RIGHT")
				send("right")
				lastAction = "right"
				lastActionTime = time.time()
				# canMove[0] = False

			if "left" in tvaction.lower():
				print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM LEFT")
				send("left")
				lastAction = "left"
				lastActionTime = time.time()
				# canMove[0] = False

			if "up" in tvaction.lower():
				print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM UP")
				send("up")
				lastAction = "up"
				lastActionTime = time.time()
				# canMove[0] = False

			if "down" in tvaction.lower():
				print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM DOWN")
				send("down")
				lastAction = "down"
				lastActionTime = time.time()
				# canMove[0] = False

			if "back" in tvaction.lower():
				if lastAction != "back" or time.time()-lastActionTime>0.8:
					print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
					send("return")
					lastAction = "back"
					lastActionTime = time.time()
					# canMove[0] = False

			if "front" in tvaction.lower():
				if lastAction != "front" or time.time()-lastActionTime>0.8:
					print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
					send("return")
					lastAction = "front"
					lastActionTime = time.time()
					# canMove[0] = False

			if "home" in tvaction.lower():
				if lastAction != "home" or time.time()-lastActionTime>0.8:
					print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
					send("home")
					lastAction = "home"
					lastActionTime = time.time()
					# canMove[0] = False

			if "volume" in tvaction.lower():
				# rt[0] = time.time()
				print("!!!!!!!!!!!!!!!!!!!!!!")
				if lastAction != "volume" or time.time()-lastActionTime>0.001:
					print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
					if withVolume:
						send("volup")
					else:
						print("VOLUME IS DISABLED IN SETTINGS")
						print()
					lastAction = "volume"
					lastActionTime = time.time()
					# canMove[0] = False

			if "wolume" in tvaction.lower():
				# rt[0] = time.time()
				if lastAction != "wolume" or time.time()-lastActionTime>0.001:
					print("DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
					if withVolume:
						send("voldown")
					else:
						print("VOLUME IS DISABLED IN SETTINGS")
						print()
					lastAction = "wolume"
					lastActionTime = time.time()
					# canMove[0] = False

			if "click" in tvaction.lower():
				# print(time.time()-lastActionTime,"***********************")
				if lastAction != "click" or time.time()-lastActionTime>0.8:
					print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
					send("enter")
					lastActionTime = time.time()
					lastAction = "click"
					# canMove[0] = False

			elif "init" in tvaction.lower():
				print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
				# send("enter")
				lastActionTime = time.time()
				lastAction = "init"
				watchlock = True

			if "unlock" in tvaction.lower():
				print("UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
				# send("enter")
				lastActionTime = time.time()
				lastAction = "unlock"
				watchlock = False
				# canMove[0] = False

			elif "lock" in tvaction.lower():
				print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")
				# send("enter")
				lastActionTime = time.time()
				lastAction = "lock"
				watchlock = True
				# canMove[0] = False
			dash()


	except Exception as e:
		 print("---------------",e)
	# else:
	# 	pass
