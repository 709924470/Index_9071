#coding = utf-8
import os,time,datetime
import os.path
from django.http import HttpResponse as hr
from django.template.loader import render_to_string as rts

cont = []
today={}
day = {}
month = {}
cdate = {}
title = {}
content = {}
img = {}
files = []
tfi = []
other = []
date = time.strftime('%Y.%m.%d')

def index_refresh():
	for p,d,fi in os.walk('.\\src\\doc\\'):
		for f in fi:
			files.append(os.path.join(p,f))
	for f in files:
		if f[-3:] == 'txt':
			tfi.append(f)
		else:
			other.append(f)
	for a in tfi:
		aa = a.split('\\')[len(a.split('\\')) - 2]
		if aa in cont:
			pass
		else:
			cont.append(aa)
		pass
		for b in other:
			if '\\'+aa+'\\' in b:
				img[aa] = b
			try:
				with open(a,'r') as c:
					cc = c.readlines()
					for cv in cc:
						ccc = cv.strip()
						if ccc.startswith('date:'):
							ccv = ccc.split(':')[1]
							today[aa] = ccv
							ca = time.strptime(ccv,'%Y/%m/%d')
							cy,cm,cd = ca[:3]
							c1 = datetime.datetime(cy,cm,cd)
							day[aa] = c1.strftime('%d')
							month[aa] = c1.strftime('%b')
							cdate[aa] = c1.strftime('%Y.%m.%d')
						elif ccc.startswith('title:'):
							title[aa] = ccc.split(':')[1]
						elif ccc.startswith('content:'):
							content[aa] = ccc.split(':')[1]
						else:
							content[aa] += ccc
			except Exception as e:
				print('error')
				print(e)
index_refresh()

def recordIP(request):
	req = request.get_full_path()
	ip = request.META['REMOTE_ADDR']
	ua = request.META['HTTP_USER_AGENT']
	with open('.\\visitor-s-ip.txt','a+') as isav:
		isav.write('[' + time.strftime('%Y-%m-%d %H:%M:%S') + '] \nUser with IP: ')
		isav.write(ip)
		isav.write(' \nVisited ' + req + ' \nBy browser ' + ua + '\n')
		isav.write('-------------------------------------------------\n')

def index(resp):
	recordIP(resp)
	index_refresh()
	con = {
		'cont':cont,
		'day':day,
		'month':month,
		'date':date,
		'today':today,
		'title':title,
		'cdate':cdate,
		'content':content,
		'img':img,
		}
	#print(con)
	return hr(rts('index.html',con))

def aboutfrc(resp):
	recordIP(resp)
	return hr(rts('frc.html'))

def aboutus(resp):
	recordIP(resp)
	return hr(rts('aboutus.html'))

def page404(resp):
	recordIP(resp)
	return hr(rts('404.html'))