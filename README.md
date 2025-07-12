# Producer-Consumer Program

This is a basic implementation of the Producer-Consumer pattern using Python's threading and Queue modules.

## How it works

- **Producer Thread**: Continuously generates random numbers (1-100) and adds them to a shared buffer
- **Consumer Thread**: Continuously removes items from the buffer and "consumes" them
- **Shared Buffer**: A Queue with a maximum size of 5 items that automatically handles synchronization

## Key Features

- **Thread Safety**: The Queue automatically handles synchronization between producer and consumer
- **Blocking Behavior**: 
  - Producer blocks when buffer is full (maxsize=5)
  - Consumer blocks when buffer is empty
- **Random Delays**: Both threads have random sleep times to simulate real-world processing
- **Infinite Loop**: Both threads run continuously until manually stopped

## Running the Program

```bash
python producer_consumer.py
```

## Expected Output

You'll see alternating output like:
```
Produced: 42
Consumed: 42
Produced: 17
Consumed: 17
Produced: 89
...
```

## Stopping the Program

Press `Ctrl+C` to stop the program execution.

## Thread Synchronization

The program demonstrates:
- **Mutual Exclusion**: Only one thread can access the buffer at a time
- **Condition Synchronization**: Producer waits when buffer is full, Consumer waits when buffer is empty
- **Bounded Buffer**: Prevents memory overflow with a maximum buffer size 