
import datetime
from random import randint as rnd
start = datetime.datetime.now()
k = 100
for i in range(10):
    a = [rnd(1,999) for i in range(2000)]

    good = []
    good_v = []
    bad = []
    for i in range( len(a)):
        to_find = k - a[i]
        if to_find in bad or a[i] in bad:
            continue
        for j in range(i,len(a)):
            
            if a[j] == to_find:
                good.append([i,j]) 
                good_v.append([a[i],a[j]]) 
        bad.append(to_find)
        bad.append(a[i])
print(datetime.datetime.now()- start)  