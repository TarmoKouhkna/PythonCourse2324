import threading
import queue
import time

# Shared queue
shared_queue = queue.Queue()


# Producer function
def producer():
    for i in range(5):
        item = i
        shared_queue.put(item)
        print(f"Produced: {item}")
        time.sleep(1)


# Consumer function
def consumer():
    while True:
        item = shared_queue.get()
        print(f"Consumed: {item}")
        shared_queue.task_done()


# Create producer and consumer threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Start the threads
producer_thread.start()
consumer_thread.start()

# Join the threads to wait for them to finish
producer_thread.join()
consumer_thread.join()
