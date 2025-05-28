import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'

splicedonor=[]
spliceacceptor=[]

for sd in re.finditer('GT', seq):
    splicedonor.append(sd.start())

for sa in re.finditer('AG', seq):
    spliceacceptor.append(sa.start())

intronlength = []
for place1 in splicedonor:
    for place2 in spliceacceptor:
        if place2 > place1:
            intronlength.append(place2 + 2 - place1) 
    
maxlength=max(intronlength)
print (f"the length of the longest intron is: {maxlength}")