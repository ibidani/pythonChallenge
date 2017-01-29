import sys
message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
message2 = "map"
translation = []
for char in message2:
    ascii = ord(char)
    # translation.append()
    if (65 <= ascii <= 90) or (97 <= ascii <= 122):
        translation.append(str(unichr(ord(char)+2)))
        # print char , "-" ,ord(char) , "-" , str(unichr(ord(char)+2))
    else:
        translation.append(char)
print translation



