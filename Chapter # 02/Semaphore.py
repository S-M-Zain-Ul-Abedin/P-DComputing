import threading
import time
from do_something import do_something  # Ensure this file exists and defines do_something(size, out_list)

def worker(thread_id, size, out_list, semaphore):
    """Worker thread that waits for a semaphore permit before executing."""
    print(f"[⏳] Thread {thread_id} waiting for permit...")
    with semaphore:
        print(f"[🚀] Thread {thread_id} started.")
        do_something(size, out_list)
        print(f"[✅] Thread {thread_id} finished.")

def run_semaphore_threads(num_threads, size, max_concurrent):
    """Initialize and run threads using a semaphore to limit concurrency."""
    out_list = []
    semaphore = threading.Semaphore(max_concurrent)
    threads = []

    # Create worker threads
    for i in range(num_threads):
        thread = threading.Thread(target=worker, args=(i, size, out_list, semaphore))
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    return out_list

if __name__ == "__main__":
    NUM_THREADS = 3
    SIZE = 7
    MAX_CONCURRENT = 2  # Allow only 2 threads to run at once

    final_output = run_semaphore_threads(NUM_THREADS, SIZE, MAX_CONCURRENT)

    print("\nFinal Output List:", final_output)
    print(f"Length of list (Semaphore): {len(final_output)}")
