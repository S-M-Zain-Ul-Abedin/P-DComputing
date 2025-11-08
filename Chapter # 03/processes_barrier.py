import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime
from do_something import do_something

def run_with_barrier(sync: Barrier, lock: Lock):
    """Process function that waits at a barrier and executes with a lock."""
    name = multiprocessing.current_process().name
    sync.wait()  # Wait for other processes at the barrier
    timestamp = datetime.fromtimestamp(time())
    with lock:  # Ensure print statements are not interleaved
        print(f"{name} ---> {timestamp}")
        output = []
        do_something(2, output)
        print(f"{name} results: {output}")

def run_without_barrier():
    """Process function that runs without barrier synchronization."""
    name = multiprocessing.current_process().name
    timestamp = datetime.fromtimestamp(time())
    print(f"{name} ---> {timestamp}")
    output = []
    do_something(2, output)
    print(f"{name} results: {output}")

def launch_processes():
    """Launches processes with and without barrier synchronization."""
    sync = Barrier(2)  # Barrier for two processes
    lock = Lock()      # Lock for safe printing

    processes = [
        Process(name="p1 - with_barrier", target=run_with_barrier, args=(sync, lock)),
        Process(name="p2 - with_barrier", target=run_with_barrier, args=(sync, lock)),
        Process(name="p3 - without_barrier", target=run_without_barrier),
        Process(name="p4 - without_barrier", target=run_without_barrier),
    ]

    # Start all processes
    for p in processes:
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

if __name__ == "__main__":
    launch_processes()
