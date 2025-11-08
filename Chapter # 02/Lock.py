import threading
import time
from do_something import do_something

def worker(thread_id, size, out_list, lock):
    """Worker thread that performs a task with thread-safe access to the shared list."""
    print(f"[+] Thread {thread_id} started.")
    with lock:
        # Ensure only one thread modifies out_list at a time
        do_something(size, out_list)
    print(f"[-] Thread {thread_id} finished.")

def run_threads(num_threads, size):
    """Create and manage multiple worker threads."""
    out_list = []
    lock = threading.Lock()
    threads = []

    # Create all threads
    for i in range(num_threads):
        thread = threading.Thread(target=worker, args=(i, size, out_list, lock))
        threads.append(thread)

    # Start each thread with a small delay for readability
    for thread in threads:
        thread.start()
        time.sleep(0.3)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    return out_list

if __name__ == "__main__":
    NUM_THREADS = 3
    SIZE = 7

    final_output = run_threads(NUM_THREADS, SIZE)

    print("\nFinal Output List:", final_output)
    print(f"Length of list (Lock): {len(final_output)}")
