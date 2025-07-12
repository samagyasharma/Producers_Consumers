import threading
import time
import random
from queue import Queue

# Shared buffer (Queue) with a maximum size of 5
buffer = Queue(maxsize=5)

# Producer thread function
def producer(producer_id):
    while True:
        item = f"P{producer_id}-{random.randint(1, 100)}"
        buffer.put(item)  # Block if buffer is full
        print(f"Producer {producer_id} -> Produced: {item}")
        time.sleep(random.uniform(0.5, 1.5))  # Random production delay

# Consumer thread function
def consumer(consumer_id):
    while True:
        item = buffer.get()  # Block if buffer is empty
        print(f"Consumer {consumer_id} <- Consumed: {item}")
        time.sleep(random.uniform(0.5, 2.0))  # Random consumption delay

# Launch multiple producers and consumers
producer_threads = []
consumer_threads = []

# Create and start 3 producer threads
for i in range(3):
    t = threading.Thread(target=producer, args=(i+1,))
    t.start()
    producer_threads.append(t)

# Create and start 3 consumer threads
for i in range(3):
    t = threading.Thread(target=consumer, args=(i+1,))
    t.start()
    consumer_threads.append(t)

# Keep the main thread alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nShutting down...") 