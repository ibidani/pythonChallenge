import pickle,pprint
pick = pickle.load(open("banner.p","r"))
for i in pick:
    print "".join([e[1] * e[0] for e in i])
file = open("out.txt","w")
obj = pickle.Unpickler(open("banner.p","r")).load()
pprint.pprint(obj)
print "hello"