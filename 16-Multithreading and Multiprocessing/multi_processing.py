## PRocesses that run in parallel
### CPU-Bound Tasks-Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing).
## PArallel execution- Multiple cores of the CPU
import multiprocessing
from multiprocessing import active_children,process

import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i * i * i}")

def numbers():
    for i in range(5):
        time.sleep(1)
        print(f"number{i}")
t=time.time()
square_numbers()
cube_numbers()
numbers()
finished_time=time.time()-t
print(finished_time)

# if __name__=="__main__":

#     ## create 2 processes
#     p1=multiprocessing.Process(target=square_numbers)
#     p2=multiprocessing.Process(target=cube_numbers)
#     p3=multiprocessing.Process(target=numbers)
#     t=time.time()

#     ## start the process
#     p1.start()
#     p2.start()
#     p3.start()
#     ## Wait for the process to complete
#     print(f'Active processes: {len(active_children())}')
#     p1.join()
#     p2.join()
#     p3.join()
#     finished_time=time.time()-t
#     print(finished_time)

