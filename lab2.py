import threading
import time
import random

class Senior:
    list = list()
    def __init__(self, var = 0.0):
        self._wage = var
    
    @property    
    def wage(self):
        lock = threading.Lock()
        lock.acquire()
        try:
            var = self._wage
        finally:
            lock.release()
            return var
    
    def set_wage(self, var):
        lock = threading.Lock()
        lock.acquire()
        try:
            self.list.append(self.wage)
            self._wage += var
        finally:
            lock.release()
            
class TeamLead:
    list = list()
    def __init__(self, var = 0.0):
        self._wage = var
    
    @property    
    def wage(self):
        lock = threading.Lock()
        lock.acquire()
        try:
            var = self._wage
        finally:
            lock.release()
            return var
    
    def set_wage(self, var):
        lock = threading.Lock()
        lock.acquire()
        try:
            self.list.append(self.wage)
            self._wage += var
        finally:
            lock.release()
            
def add(element, var):
    for i in range(var):
        num = random.random()
        element.set_wage(num)
        
S = Senior()
TL = TeamLead()

rand_num1 = random.randint(10000, 20000)
rand_num2 = random.randint(10000, 20000)
print("Num1: ", rand_num1, "Num2: ", rand_num2)

start = time.time()
threads = list()
rand_num_thread = random.randint(10, 20)

for number in range(rand_num_thread):
    if number < rand_num_thread / 2:
        even_thread = threading.Thread(target=add, args=(S, rand_num1)) # Передаємо до потоку функцію, та змінні для неї
        threads.append(even_thread)
        threads[-1].start() # Запуск останнього доданого потоку
    else:
        odd_thread = threading.Thread(target=add, args=(TL, rand_num2))
        threads.append(odd_thread)
        threads[-1].start()
    
for thread in threads:
        thread.join()
        
finish = time.time()
print("Senior wage: ", S.wage, ", Team Lead wage: ", TL.wage)
print("Runtime: ", (finish - start))