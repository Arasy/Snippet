# pip install pytube  (https://github.com/nficano/pytube)
# pip install bs4
# pip install urllib2

from pytube import YouTube as YT
import urllib2
from random import randint
import time
import pickle
from datetime import datetime
from bs4 import BeautifulSoup as BS
import os
import re
import wget

def grabmp4(url):
   try :
      yt = YT(url)
      stream = yt.streams.first()
      namafile = re.sub(r'[\\/*?:"<>|]','',str(yt.title))+".mp4"
      if (os.path.exists(lokasi+'/'+namafile)):
         print "File",str(yt.title),"exists, skipping download"
      else:
         print "Downloading", yt.title
         logfile.append(str(datetime.now())+ " Start downloading "+ str(yt.title))
         stream.download(lokasi)
         logfile.append(str(datetime.now())+ " Finish downloading "+ str(yt.title))
   except Exception as e:
      print "Cannot download", url," reason =", e
      logfile.append(str(datetime.now())+ " Cannot download "+ url+ " reason = "+ str(e))
   
def getpdf(url):
    wget.download(url, bar=bar_thermometer)

def delay():
    #delaying
    jeda = randint(10,100)
    jeda = 1.0/jeda
    jeda = randint(0,2)+jeda
    time.sleep(jeda)
    print "Waiting... ",jeda, "seconds"
    logfile.append(str(datetime.now())+ " Delaying "+ str(jeda)+ " seconds")


#inisialisasi

listvideo = []
listpdf = []
logfile = []
logfile.append("Start at "+str(datetime.now()))
listofplaylist = [("https://www.youtube.com/playlist?list=PL3FW7Lu3i5Jsnh1rnUwq_TcylNr7EkRe6","NLPDeepLearning")]

for playlist,folderlok in listofplaylist:
    lokasi = os.getcwd()+'/'+folderlok
    if(not os.path.exists(lokasi)):
        os.makedirs(lokasi)
    laman = urllib2.urlopen(playlist, timeout = 5).read()
    links = BS(laman).find_all('a')

    for i in links :
        link = i['href']
        # get youtube video file
        if('youtube' in link and 'watch' in link):
            awal = link.find('&')
            link = link[:awal]
            if link[0] == '/':
               link = "https://www.youtube.com"+link
            listvideo.append(link)
        # get pdf file
        if('.pdf' in link):
            listpdf.append(link)

    for i in listvideo:
        grabmp4(i)
        delay()

    for i in listpdf:
        getpdf(i)
        delay()

    pickle.dump(logfile, open("log"+folderlok+".p", "wb"))

