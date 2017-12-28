#coding=utf-8
import time
import requests
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
url = "http://www.xiaohuar.com/list-1-1.html"
print "Start : %s" % time.ctime()
response = requests.get(url)
html = response.text
img_urls=re.findall(r"/d/file/\d+/\w+\.jpg",html)
for img_url in img_urls:
    print(img_url)
    img_response = requests.get("http://www.xiaohuar.com%s" %img_url)
    img_data = img_response.content
    xiaohua = img_url.split('/')[-1]
    with open(xiaohua,'wb') as f:
        f.write(img_data)
        time.sleep(5)
        print("down success!")
        f.close
    os.system ("copy %s %s" %(xiaohua,r'C:\Users\cdv\Pictures\%s' %xiaohua))
    time.sleep(6)
    if os.path.exists(xiaohua):
        print("正在删除 %s" %xiaohua)
        os.system("del %s" %xiaohua)
        
