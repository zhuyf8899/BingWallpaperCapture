#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
#author:zhuyifan
import urllib  
import urllib2
import cookielib
import re
import sys
import os
import platform
import time

class GetWallpaper(object):
    def __init__(self, path):
        super(GetWallpaper, self).__init__()
        self.filePath = path
    def get(self):
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        req = urllib2.Request(
            url = 'http://www.bing.com/?mkt=zh-CN'
        )
        htmlData = ""
        htmlData = opener.open(req).read()
        if htmlData:
            #reString = 'background-image: url("\w*")'
            reString = 'url:[^,]*\.jpg'
            imgUrl = re.search(reString,htmlData).group()
            imgUrl = imgUrl[6:]
            imgUrl = imgUrl.replace('\\','')
            #print self.filePath
            #print 'DEBUG: the url is: ' +　imgUrl
            try:
                fileName = time.strftime('%Y_%m_%d.jpg',time.localtime(time.time()))
                urllib.urlretrieve(imgUrl,self.filePath+fileName)
            except Exception, e:
                print str(e) + ' exit...'
                exit(-4)
            
if __name__ == '__main__':
    #print os.environ['USERNAME']
    system = platform.system()
    #exit()
    path = ''
    if system == 'Windows':
        if len(sys.argv) == 1:
            path = 'C:\\Users\\%s\\Pictures\\'%(os.environ['USERNAME'])
        else:
            if os.path.isdir(sys.argv[1]):
                path = sys.argv[1]
                if path[-1:] != '/':
                    path += '/'
            else:
                print "%s is not a dirtory, exit..."%(sys.argv[1])
                exit(-1)
    elif system == 'Linux':
        if len(sys.argv) == 1:
            path = '/home/%s/wallpaper/'%(os.environ['USER'])
            if not os.path.isdir(path):
                try:
                    os.makedirs(path)
                except Exception, e:
                    print str(e) + ' exit...'
                    exit(-2)
        else:
            if os.path.isdir(sys.argv[1]):
                path = path = sys.argv[1]
            else:
                print "%s is not a dirtory, exit..."%(sys.argv[1])
                exit(-1)
    elif system == 'Darwin':
        if len(sys.argv) == 1:
            path = '/home/%s/Downloads/wallpaper/'%(os.environ['USER'])
            if not os.path.isdir(path):
                try:
                    os.makedirs(path)
                except Exception, e:
                    print str(e) + ' exit...'
                    exit(-2)
        else:
            if os.path.isdir(sys.argv[1]):
                path = path = sys.argv[1]
                if path[-1:] != '/':
                    path += '/'
            else:
                print "%s is not a dirtory, exit..."%(sys.argv[1])
                exit(-1)
    else:
        print "Unsupported operating, exit..."
        exit(-3)
                
    example = GetWallpaper(path)
    example.get()
    print('done.')
