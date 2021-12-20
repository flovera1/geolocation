#!/usr/bin/python
# -*- coding: utf8 -*-
# NOTE: the script works, but the twitter keys need to incorporated. Lines 18-21 and lines 25-28
import sys, codecs
import twitter
from time import sleep
from shapely.geometry import MultiPoint
from datetime import datetime
from xml.dom.minidom import parse
from xml.sax.saxutils import escape

import time
import timeout_decorator


apis=[]

api1 = twitter.Api(consumer_key='',
    consumer_secret='',
    access_token_key='',
    access_token_secret='',
    sleep_on_rate_limit=True)

#farideh
api2 = twitter.Api(consumer_key='',
    consumer_secret='',
    access_token_key='',
    access_token_secret='',
    sleep_on_rate_limit=True)

apis.append(api1)
apis.append(api2)

t_ids=[]

#@timeout_decorator.timeout(5)
def getStatus(api, id):
	return api.GetStatus(id)
	
InpFile=codecs.open(sys.argv[1], "r", "utf-8")
for line in InpFile.readlines():
    id=line.strip()
    t_ids.append(id)
InpFile.close()

n_dl=0
n_negated=0

i=0
mlen=len(t_ids)
#TODO: da verificare e completare
Ofile=codecs.open(sys.argv[2]+".tsv", "w", "utf-8")
Ofile.write("id\tuser_screen_name\ttext\tplace_name\tlon\tlat\n")
while i < mlen:
    id=t_ids[i]
    r= i % 2
    api=apis[r]
    try:
        #status = api.GetStatus(id)
        status=getStatus(api, id)
        js=status.AsDict()
        try:
          coords=js['coordinates']['coordinates']
          #print js['place']['full_name'], coords[0], coords[1] #lon, lat
        except KeyError:
          try:
            bbox=js['place']['bounding_box']
          except:
            i+=1
            continue
          coords=bbox['coordinates']
          mpstr=[]
          for point in coords[0]:
            mpstr.append((point[0], point[1]))
          mp=MultiPoint(mpstr)
          coords = [mp.centroid.x, mp.centroid.y]
          #print js['place']['full_name'], bbox
        #print id, js['user']['screen_name'], js['text'], js['place']['full_name'], coords[0], coords[1]
        text=js['text'].replace('"','')
        text=text.replace('\n', ' ')
        try:
          Ofile.write(id+'\t"@'+js['user']['screen_name']+'"\t"'+text+'"\t"'+js['place']['full_name']+'"\t'+str(coords[0])+'\t'+str(coords[1]))
          Ofile.write("\n")
        except KeyError:
          pass
        n_dl+=1
        i+=1
    except twitter.error.TwitterError as err:
        if err.message[0]['code']==88:
            print id, err.message[0]['message']
            print "waiting..."
            sleep(960) #windows of 15 minutes
            print "retrying..."
        else:
            print id, err.message[0]['message'], "code:"+str(err.message[0]['code'])
            i+=1
            n_negated+=1
    sys.stdout.flush()
Ofile.close()

print "downloaded:", n_dl
print "not allowed:", n_negated
