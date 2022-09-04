import re
import random

def unique(logedIssues):
    unique_list=[]
    for x in logedIssues:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

ismertszavak=[]
with open('ismertszavak.txt','r') as file2:
    for line2 in file2:
        ismertszavak.append(line2.split()[0])

szokeszlet=[]
    

with open('South.Park.The.Streaming.Wars.Part.2.2022.WEBRip.x264-ION10.Hi.srt','r') as file:
   
        # reading each line    
        for line in file:
            line=re.sub("</font>","", line)
            line=line.replace("- ","")
            line=line.replace(",","")
            line=line.replace(".","")
            line=line.replace("!","")
            line=line.replace("?","")
            line=line.replace("</i>","")
            line=line.replace("<i>","")
            line=line.replace('"',"")
            line=line.replace('*',"")
            line=line.replace(':',"")
            line=line.replace(')',"")
            line=line.replace('(',"")
            
            line=re.sub("color=#(?:[0-9a-fA-F]{3}){1,2}"," ", line)
            line=line.replace(' >',"")
            # reading each word        
            for word in line.split():
                nem=True
                if (not re.match("\d\d\:\d\d\:\d\d\,\d\d\d", word)) and (not re.match("\d", word)) and (not re.match("-->", word))  and (not re.match("<font", word)):
                    for ismertszo in ismertszavak:
                        if str(word.lower()) == ismertszo:   
                            nem=False
                    if(nem):
                        szokeszlet.append((word.lower()))

#random.shuffle(szokeszlet)
szokeszlet=unique(szokeszlet)
with open('ismeretlenSZavak.txt', 'w') as f:
    f.write("")
for szo in szokeszlet:
    with open('ismeretlenSZavak.txt', 'a') as f:
        f.write(szo + "\n")