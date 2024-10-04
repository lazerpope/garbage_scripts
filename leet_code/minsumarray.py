a = [2,-3,5,-4,9,-1,-2,2,-9]

min_sum =  a[0]
last = a[0]

for i in range(1,len(a)):
    current = min(a[i],a[i]+last)    
    min_sum = min(min_sum,current)
    last = current

print(min_sum)