import time
import asyncio
import aiohttp

async def do(s , res ):
    try:
        start = time.perf_counter()
        print('started request number:',s)
    
        async with aiohttp.ClientSession() as session:
            url = 'http://5.35.84.79:80'
            async with session.get(url) as resp:            
                await resp.text() 
                finish = round(time.perf_counter()-start,3)
                res[s] = finish
                print('finished request number:',s , resp.status)
    except:
        res[s] = 'err'
    

async def main():
    start_total =  time.perf_counter()
    res = {}
    tasks = [asyncio.create_task(do(s , res)) for s in range(50)]
    await asyncio.gather(*tasks)   
    end_total =  time.perf_counter()
    print(f'finished in {end_total-start_total} seconds')
    print(res)

if __name__ == '__main__':
    asyncio.run(main())


# finished in 20.56269459996838 seconds
# п = {7: 10.433, 4: 11.373, 3: 11.517, 1: 11.865, 23: 12.994, 13: 13.029, 5: 13.52, 16: 13.545, 10: 13.566, 11: 13.855, 6: 13.957, 2: 14.068, 15: 14.17, 21: 14.288, 0: 14.52, 18: 14.765, 8: 14.814, 20: 15.049, 17: 15.159, 12: 15.196, 9: 15.265, 14: 15.321, 42: 15.336, 35: 15.478, 30: 15.6, 19: 15.632, 39: 15.631, 28: 15.693, 24: 15.855, 37: 15.948, 49: 16.032, 41: 16.048, 38: 16.206, 36: 16.335, 22: 16.352, 47: 16.501, 46: 16.719, 48: 16.72, 25: 16.79, 27: 16.833, 44: 17.093, 43: 17.154, 34: 17.242, 32: 17.318, 26: 17.336, 31: 17.361, 33: 17.42, 29: 17.98, 45: 18.678, 40: 20.546}