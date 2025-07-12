import threading
import time
import random
from queue import Queue

# Shared buffer (Queue) with a maximum size of 5
buffer = Queue(maxsize=5)

# Producer thread function
def producer():
    while True:
        item = random.randint(1, 100)  # Generate a random item
        buffer.put(item)  # Block if buffer is full
        print(f"Produced: {item}")
        time.sleep(random.uniform(0.5, 1.5))  # Random production delay

# Consumer thread function
def consumer():
    while True:
        item = buffer.get()  # Block if buffer is empty
        print(f"Consumed: {item}")
        time.sleep(random.uniform(0.5, 2.0))  # Random consumption delay

# Create and start the threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start() 