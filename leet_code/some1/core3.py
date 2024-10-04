a = [4, -4, 6, 2, -19, 7, 9, -9, 6, 8]

max_sum = sum(a)
sta = 0
end = 0
for i in range(0, len(a)-1):
    for j in range(i+1,len(a)):
        sub = []
        for k in range(i,j+1):
            sub.append(a[k])
        sub_sum = sum(sub)
        if  sub_sum > max_sum:
            sta = i
            end = j
            max_sum =  sub_sum 
sub = []
for k in range(sta,end+1):
    sub.append(a[k])
sub_sum = sum(sub)
print(sub)
print(max_sum)