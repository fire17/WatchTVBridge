#
# Based on an original code by Ape on GitHub: https://github.com/Ape/samsungctl
# -- Roozbeh Farahbod, March 2020
#

import base64
import json
import logging
import time
import ssl





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

try:
	import websocket
except ImportError:
	install('websocket-client')
	import websocket
# import websocket
from threading import Thread

# Available Keys:
#  - KEY_POWER
#  - KEY_HOME
#  - KEY_MENU
#  - KEY_SOURCE
#  - KEY_GUIDE
#  - KEY_TOOLS
#  - KEY_INFO
#  - KEY_UP
#  - KEY_DOWN
#  - KEY_LEFT
#  - KEY_RIGHT
#  - KEY_ENTER
#  - KEY_RETURN
#  - KEY_CH_LIST
#  - KEY_CHUP
#  - KEY_CHDOWN
#  - KEY_VOLUP
#  - KEY_VOLDOWN
#  - KEY_MUTE
#  - KEY_RED
#  - KEY_GREEN
#  - KEY_YELLOW
#  - KEY_BLUE

# MediaPlayPause

class SamsungTV():
	format_ws = 'ws://{host}:{port}/api/v2/channels/samsung.remote.control?name={name}'
	format_wss = 'wss://{host}:{port}/api/v2/channels/samsung.remote.control?name={name}'
	_URL_FORMAT = format_wss
	readback = False

	_KEY_GAP_S = 0.1

	logger = logging.getLogger('samsungTV')


	def __init__(self, host, port=8002, name='SamsungTvRemote', read = False):
		try:
			self.readback = read
			# if port == 8001:
			# 	self._URL_FORMAT = self.format_ws
			print("!!!!!!!")
			print(self._URL_FORMAT)
			print(host,port)
			ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
			self.connection = ws
			self.connection.connect(
				self._URL_FORMAT.format(**{
					'host': host,
					'port': port,
					'name': self._serialize_string(name)
				})
			)
			# if self.readback:
			#     t = Thread(target = self._read_response, args = [None,])
			#     t.start()

		except Exception as err:
			self.logger.error('Websocket connection failed. Error: {}'.format(err))
			self.connection = None
		else:
			self.logger.info('Websocket connection established.')

	def __exit__(self, type, value, traceback):
		# self.close()
		pass

	def _serialize_string(self, string):
		if isinstance(string, str):
			string = str.encode(string)
		return base64.b64encode(string).decode('utf-8')

	def close(self):
		pass
		# if self.connection:
		#     self.connection.close()
		#     self.connection = None
		#     self.logger.info('Connection closed.')

	def send_key(self, key, repeat=1):
		print("@@@@@@@@ KEY",key)
		if self.connection:
			for n in range(repeat):
				payload = json.dumps({
					'method': 'ms.remote.control',
					'params': {
						'Cmd': 'Click',
						'DataOfCmd': key,
						'Option': 'false',
						'TypeOfRemote': 'SendRemoteKey'
					}
				})

				try:
					self.connection.send(payload)
				except Exception as err:
					self.logger.error('Could not send the key. Error: {}'.format(err))
					raise Exception("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
				else:
					self.logger.info('Sent {} key to the TV.'.format(key))
					time.sleep(self._KEY_GAP_S)

	def _read_response(self, datat):
		response = self.connection.recv()
		response = json.loads(response)

		if response["event"] != "ms.channel.connect":
			self.close()
			self.logger.error('Could not read from the channel. Reason: {}', response)

		logging.debug("Access granted.")
