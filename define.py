#!/user/python3
'''
author:   linfeng
date:     2020/2/12

'''
import requests


# set the url
url = "http://www.baidu.com"

# set the filename
filename = "~/pachong/file.txt"

#define a class about script
class script():
    def __init__(self, method="Text"):
        self.url = url
        #the method can be image, text ,directory and so on
        self.method = method
        #the content is used to buff the data
        self.content = []

    def run(self):
        self.content.append(requests.get(self.url).text)
        '''
        write the headinfo
        '''
        print("########   HEAD    ########")
        print()
        print("url     = ",self.url)
        print("method  = ",self.method)
        print()
        print("########   END     ########")
        '''
        write the content
        '''
        print("########   CONTENT ########")
        print()
        print(self.content)
        print()
        print("########   END     ########")




