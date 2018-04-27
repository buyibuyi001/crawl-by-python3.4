import re
import os
import urllib
from urllib import request

def getPage(url):

    hearders={}
    #req=urllib.request.Request(url,hearder=headers)
    stream=urllib.request.urlopen(url)
    page=stream.read().decode('UTF-8')
    return page     #firsr decode and then findall,success or fail

def getImg(page):

    reg = r'src="(.+?\.jpg)" pic_ext'
    #reg = r'src="(.+?\.png)"'
    #reg = r'file="(.+?\.jpg)"'
    imgre=re.compile(reg)
    print("start crawling")

    f=open("getImg.txt",'w+')
    imglist=re.findall(imgre,page)

    for i in imglist:
        f.write(i+'\n')    #\n valid

    x=0
    path="picture"
    if not os.path.isdir(path):
        os.makedirs(path)
    paths=path+"\\"

    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'{}{}.jpg'.format(paths,x))
        x=x+1
    print ('crawling finished')
    return imglist
def main():

    url="https://tieba.baidu.com/p/2460150866"
    page = getPage(url)
    while not page:
        getImg(page)

if __name__=="__main__":
    main()


