import threading
import time
import random

# Shared buffer with max size
buffer = []
BUFFER_SIZE = 5

# Lock and condition variable
lock = threading.Lock()
condition = threading.Condition(lock)

# Producer thread function
def producer(producer_id):
    while True:
        item = f"P{producer_id}-{random.randint(1, 100)}"

        with condition:
            while len(buffer) == BUFFER_SIZE:
                print(f"Producer {producer_id} waiting: Buffer full")
                condition.wait()  # wait until space is available

            buffer.append(item)
            print(f"Producer {producer_id} -> Produced: {item} | Buffer: {buffer}")
            condition.notify()  # signal a consumer

        time.sleep(random.uniform(0.5, 1.5))

# Consumer thread function
def consumer(consumer_id):
    while True:
        with condition:
            while len(buffer) == 0:
                print(f"Consumer {consumer_id} waiting: Buffer empty")
                condition.wait()  # wait until item is available

            item = buffer.pop(0)
            print(f"Consumer {consumer_id} <- Consumed: {item} | Buffer: {buffer}")
            condition.notify()  # signal a producer

        time.sleep(random.uniform(0.5, 2.0))

# Start threads
for i in range(2):
    threading.Thread(target=producer, args=(i+1,), daemon=True).start()

for i in range(2):
    threading.Thread(target=consumer, args=(i+1,), daemon=True).start()

# Keep main thread alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nShutting down...") 