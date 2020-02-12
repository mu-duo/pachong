'''
get all var from the file named define.py
'''
import define

#import the module
import requests
import re
import json

c =define.script()
print("the method is",c.method)
c.run()
