import datetime
from random import randint as rnd
a = [4, -4, 6, 2, -19, 7, 9, -9, 6, 8]
start = datetime.datetime.now()
k = 100
for i in range(10):
    a = [rnd(1,999) for i in range(2000)]


    
    
    good = []
    good_v = []
    for i in range( len(a)):
        for j in range(i,len(a)):
            if a[i]+a[j] == k:
                good.append([i,j]) 
                good_v.append([a[i],a[j]]) 
 
# print(good_v)
# print(good)
print(datetime.datetime.now()- start)  