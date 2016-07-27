from bs4 import BeautifulSoup
import urllib2
from datetime import *
import time
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = 'http://www.zhibo8.cc/'
q = urllib2.urlopen(url)
soup = BeautifulSoup(q,'lxml')

i = date.today()
today = soup.find(title=i)
# today1 = soup.find_all(class_='content')
# for i in today1:
#    print i.li
print soup

# today1 = today.next.next.next.next
# for i in today1.ul:
#     if i.next.string == None:
#         pass
#     else:
#         print i.next.string + '\n' + i.next.next.string
#         print '-'*30
