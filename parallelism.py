```python
import multiprocessing
import time

def some_function():
    print("Starting some_function in parallelism.py")

    # Create two processes
    process1 = multiprocessing.Process(target=worker, args=("Process-1", 2))
    process2 = multiprocessing.Process(target=worker, args=("Process-2", 4))

    # Start new Processes
    process1.start()
    process2.start()

    # Wait for both processes to complete
    process1.join()
    process2.join()

    print("Exiting some_function in parallelism.py")

def worker(process_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"{process_name} {time.ctime(time.time())}")
```
