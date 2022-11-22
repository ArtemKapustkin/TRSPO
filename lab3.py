import time
from concurrent.futures import ThreadPoolExecutor
import random

def collatz(num):
    list = []
    while num != 1:
        if num % 2 == 0:
            num = int(num / 2)
            list.append(num)
        else:
            num = int(3 * num + 1)
            list.append(num)
    return list

def threat_collatz(numbers, w, p):
    start = time.time()
    executor = ThreadPoolExecutor(max_workers=w)
    futures = []
    for x in sorted(numbers):
        futures.append(executor.submit(collatz, x))
    for future in futures:
        future.result()
    finish = time.time()
    print("Loop pass #"+str(p)+": ",(finish - start))

numbers = []
rand_int = random.randint(500, 1000)
for i in range(rand_int):
    numbers.append(i + 1)
    
print("ThreadPoolExecutor with max_workers=1:")
for i in range(5):
    threat_collatz(numbers, 1, i)
print("\nThreadPoolExecutor with max_workers=8")
for i in range(5):
    threat_collatz(numbers, 8, i)