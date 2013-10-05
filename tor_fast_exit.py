#AUTHOR: sampox
#This python script will find the fastest python exit nodes by fetching
#the information straight from the server listing

import urllib,re

f=urllib.urlopen("http://torstatus.blutmagie.de/index.php","SR=Bandwidth&SO=Desc&FFast=1&FExit=1&FStable=1&FValid=1&FBadExit=0")

data=f.read()
ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}',data)

from collections import OrderedDict
NoDoubles = list(OrderedDict.fromkeys(ip))
#print NoDoubles[:15]

for i in range(1,21):
	x=NoDoubles[i]
	if(x[0]!=0 and x[0]!='0'):
		print x

