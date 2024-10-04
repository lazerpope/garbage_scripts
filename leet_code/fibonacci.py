def fib(n):
    global calls
    calls +=1
    if n == 0:
        return 0
    if n == 1:
        return 1
    if  n == 2:
        return 1
    
    return fib(n-1) + fib(n-2) 

def cfib(n, cache={}):
    global calls
    calls +=1
    if n == 0:
        return 0
    if n == 1:
        return 1
    if  n == 2:
        return 1
    
    if n in cache.keys():
        return cache[n]

    res = cfib(n-1,cache) + cfib(n-2,cache) 

    if not n in cache.keys():
        cache[n] = res

    return res


import time
calls = 0
# Start the timer
start_time = time.time()

# print(fib(30))
print(cfib(300))
print(calls)

elapsed_time = time.time() - start_time

print(elapsed_time)