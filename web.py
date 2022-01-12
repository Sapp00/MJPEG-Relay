import requests
import http.server
import socketserver

import configparser
import threading

import time
import os

from shutil import copyfile

def refresh(url, name):
	while True:
		r = requests.get(url)
		#print(r.headers.get('content-type'))
		with open('html/cache/'+name+'.jpg', 'wb') as f:
			f.write(r.content)
		time.sleep(0.8)

def clear():
	dir = 'html/streams'
	for f in os.listdir(dir):
		os.remove(os.path.join(dir, f))


class Relay:
	def __init__(self, name):
		self.name = name
		self.port = int(config.get(name, 'RelayPort'))
		self.silence = config.get(name, 'Silence')
		self.debugging = config.get(name, 'Debugging')
		self.url = config.get(name, 'StreamSourceURL')
		self.refreshRate = int(config.get(name, 'RefreshRate'))

	def setIndex(self):
		templatefile = "html/template.html"
		indexfile = "html/streams/"+self.name+".html"
		copyfile(templatefile,indexfile)

		with open(templatefile, 'r') as t:
			t_data = t.read()
			i_data = t_data.replace("#NAME#", self.name)

		with open(indexfile, 'w') as i:
			i.write(i_data)

	def exec(self):
		x = threading.Thread(name=self.name, target=refresh, args=(self.url, self.name))
		x.setDaemon(True)
		x.start()
		self.setIndex()

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="html", **kwargs)

def startServer():
	with socketserver.TCPServer(("", 80), MyHandler) as httpd:
		print ("Site is running.")
		httpd.serve_forever()


config = configparser.ConfigParser()
config.read("relay.conf")

clear()

sections = config.sections()

for sec in sections:
	r = Relay(sec)
	r.exec()

startServer()