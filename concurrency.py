```python
import threading
import time

def some_function():
    print("Starting some_function in concurrency.py")

    # Create two threads
    thread1 = threading.Thread(target=worker, args=("Thread-1", 2))
    thread2 = threading.Thread(target=worker, args=("Thread-2", 4))

    # Start new Threads
    thread1.start()
    thread2.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()

    print("Exiting some_function in concurrency.py")

def worker(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"{thread_name} {time.ctime(time.time())}")
```
