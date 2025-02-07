### Multithreading
## When to use Multi Threading
###I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
###  Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time
from threading import active_count

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

#With threads
##create 3 threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)
t3=threading.Thread(target=print_letter)

t=time.time()
## start the thread
t1.start()
t2.start()
t3.start()
print(f"number of threads: {active_count()}")
### Wait for the threads to complete
t1.join()
t2.join()
t3.join()

finished_time=time.time()-t
print(finished_time)



# #Without using threads
# t=time.time()
# print_numbers()
# print_letter()
# finished_time=time.time()-t
# print(finished_time)