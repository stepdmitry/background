# -*- coding: utf-8 -*-
import sys
import pycurl  
import os
import io 
import re
import subprocess
import random
import socket
import time

def _callOsProcess(_command):
	print ( u'Происходит вызов внешней утилиты/скрипта.\nИспользована команда: '+_command)
	pipe=subprocess.PIPE
	result=subprocess.Popen(_command, shell=True, stdin=pipe, stdout=pipe)
	result.wait()
	return  result.communicate()[0]

def fillbg():	
	s=_callOsProcess('curl http://getwall.ru/category/nature/page_'+str(int(random.uniform(1, 606))))
	s=s.decode('utf-8')
	p = re.compile('href="/wallpaper/\d*/')
	path= p.findall(s)[int(random.uniform(0, 30))]
	path = path[17:len(path)-1]

	s=_callOsProcess('curl http://getwall.ru/wallpaper/'+path)
	s=s.decode('utf-8')
	p = re.compile('href="/download/'+path+'/\d*x\d*/')
	path=p.findall(s)[0]
	path = path[7:len(path)-1]

	s=_callOsProcess('curl http://getwall.ru/'+path)
	s=s.decode('utf-8')
	p = re.compile('/image/\w*/\w*.\w*')
	path=p.findall(s)[0]

	s=_callOsProcess('curl -o bg.jpg http://getwall.ru'+path)
	os.system(r'gsettings set org.gnome.desktop.background picture-uri file:////home/dmitry/Документы/bg.jpg')

while 1:
	try:
		socket.gethostbyaddr('www.yandex.ru')
	except socket.gaierror:
		continue
	fillbg()
	time.sleep(3600)





#http://getwall.ru/download/143572/1920x1080/         href="/download/143572/3600x2400/
#os.startfile(r'gsettings set org.gnome.desktop.background picture-uri file:////home/proubuntucomua/wallpaper/image.png')
#http://getwall.ru/image/00c65e2d8d411ba1a39b6f8648cdc19c/getwall_ru_22_143449_1920x1080.jpg
#/image/4a255eb98b7e56c7ae55854e4ada614e/getwall_ru_22_143572_1920x1080.jpg";
