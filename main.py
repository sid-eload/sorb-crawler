import requests
from bs4 import BeautifulSoup
import operator
from collections import OrderedDict

#Crawls out a link and should return post count

url = "https://forum.sorbmc.com/index.php?topic=12728"

r = requests.get(url)

if r.status_code == 200:
	data = BeautifulSoup(r.text, 'html.parser')



	users =[]
	d ={}
	cnt = 1

	
	filt_count = data.find_all("a", { "class" : "navPages"})
	
	for n in filt_count:
		#print a.text
		if n.text > cnt:
			cnt = n.text
			#print cnt

	print 'Total Pages :',cnt
	#print filt
	term =0
	count = int(cnt)
	for i in range(0,count):
		term = 15*i
		url2 = url +"." + str(term)
		#print url2
		print term
		r2 = requests.get(url2)	
		data2 = BeautifulSoup(r2.text, 'html.parser')
		filt = data2.find_all("h4", { "class" : "perfiltitle" })


		for f in filt:
			#print f.a.text
			try:
				if f.a.text in d:
					d[f.a.text]+=1
				else:
					d[f.a.text]=1

			except:
				if f.text in d:
					st = str(f.text)
					st = st.strip()
					d[st]+=1
				else:
					st = str(f.text)
					st = st.strip()
					d[st]=1

	#newA = dict(sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
	d_d = OrderedDict(sorted(d.items(), key=lambda kv: kv[1], reverse=True)[:10])				
	for key in d_d:
		print key, d_d[key]
	#print sorted_x.reverse()
else:
	print 'something wrong. try again later kiddo'
	
#print r.text