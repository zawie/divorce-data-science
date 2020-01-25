import multiprocessing
import time

def somethingHard(arg):
    total = 0
    for i in range(arg):
        total += i

t0 = time.time()
somethingHard(10000000)
t1 = time.time()
print(round(t1-t0,2),"seconds taken for one.")

t0 =  time.time()
processes = []
for i in range(100):
        p = multiprocessing.Process(target=somethingHard,args=[10000000])
        p.start()
        processes.append(p)
for process in processes:
        process.join()

t1 = time.time()
print(round(t1-t0,2),"seconds taken for multiprocessing.")