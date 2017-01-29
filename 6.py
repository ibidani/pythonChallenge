import re,zipfile

nextnum = 90052
myzip = zipfile.ZipFile("channel.zip")

for i in range(0,1000):
    print myzip.getinfo(str(nextnum)+".txt").comment
    temp = myzip.read(str(nextnum)+".txt")
    nextnum = re.findall("(\d+)", temp)[0]
    # print i
    # print temp
