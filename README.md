# crawl-by-python3.4
import urllib.request
import re
import os
import urllib


def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()    
    return html.decode("UTF-8")

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    print("crawl")
    
    f=open("getImg.txt",'w+')
    for i in imglist:
        f.write(i+'\n')
    
    x=0
    path="picture"
    if not os.path.isdir(path):
        os.makedirs(path)
    paths=path+"\\"
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'{}{}.jpg'.format(paths,x))
        x=x+1
    return imglist

html = getHtml("http://tieba.baidu.com/p/2460150866")
getImg(html)
print ('fnished')
