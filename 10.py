from itertools import groupby
def look_and_say(num):
    return ''.join(str(len(list(g))) + str(d) for d, g in groupby(num))

pcurl = 'http://www.pythonchallenge.com/pc/return/'

number = '1'
for iter in xrange(30):
    number = look_and_say(number)

print "The next url is {0}{1}.html".format(pcurl, len(number))