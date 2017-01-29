import urllib2
import re


nextnum = 'and the next nothing is 0'
for i in range(0, 400):
    a = re.findall("(\d+)", nextnum)[0]
    res = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(a))
    nextnum = res.read()
    print(nextnum)
