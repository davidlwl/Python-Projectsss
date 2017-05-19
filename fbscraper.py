import json
import datetime
import csv
import time
import datetime
import sys
import webbrowser
from datetime import timedelta

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

app_id = ""
app_secret = ""  # DO NOT SHARE WITH ANYONE!
page_id = "TheStraitsTimes", "9gag"
now = datetime.datetime.now()
access_token = app_id + "|" + app_secret
url1 ='
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd) #change emoticons
yest = now + timedelta(days=-1)

def request_until_succeed(url):
    req = Request(url)
    success = False
    while success is False:
        try:
            response = urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception as e:
            print(e)
            time.sleep(5)

            print("Error for URL {}: {}".format(url, datetime.datetime.now()))
            print("Retrying.")

    return response.read()

def straits():
    url1 =''
    
    print(now.strftime("%Y-%m-%d"))
    link1 = []
    statuses = json.loads(request_until_succeed(url1))
    for i in statuses['data']:
        if i["reactions"]["summary"]['total_count'] > 500:
            if i["created_time"][:10] == yest.strftime("%Y-%m-%d"): #replace with todays date
                link1.append(i["link"])
                da = len(link1)
                print(str(da)+ '. ' +i["message"].translate(non_bmp_map))
                print(i["reactions"]["summary"]['total_count'])
                try:
                    if summarize(text, 2) == None:
                        pass
                    else:
                        for s in summarize(text, 2):
                            print (s)
                except ValueError:
                    pass
                print('-' *60)
               
    
def gag():
    url2 =''
    link2 = []
    print(now.strftime("%Y-%m-%d"))

    statuses = json.loads(request_until_succeed(url2))
    for i in statuses['data']:
        if i["reactions"]["summary"]['total_count'] > 30000:
            if i["created_time"][:10] == yest.strftime("%Y-%m-%d"):
                link2.append(i["link"])
                
    for x in link2:
        webbrowser.open_new_tab(x)
    
straits()
input('onto the fun stuff!')
gag()


