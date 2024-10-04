


def jj3(j, st):

    c = 0
    j = set(j)
    
    for s in st:
        if s in j:
            c+=1 
    return c


def jj4(j, st):  
    j = set(j)    
    return len([0 for s in st if s in j])

from time import perf_counter_ns
j = ''.join(['g' for i in range(5000)])+'aaAAbaaaaaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
s = ''.join(['qwertyuiopasdfghjklzxcvbnmQWERTYUIOPAZSDFGHJKL;ZXCVBNM,' for i in range(1_0_000)])
# s = 'aaAAhhhhhhhhhhhhhhhhhhhhhAb'

st = perf_counter_ns()

for i in range(100):
    # print(jj3(j,s))
    jj4(j,s)

end = perf_counter_ns()

print((end-st)//100000/10, 'ms' , )