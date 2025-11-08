import threading
import time
from do_something import do_something  # Make sure this module exists and defines the function

def worker(thread_id, size, out_list, rlock):
    """Thread worker demonstrating reentrant lock (RLock) behavior."""
    print(f"[+] Thread {thread_id} started.")
    with rlock:
        # Same thread can safely acquire the lock again
        with rlock:
            do_something(size, out_list)
    print(f"[-] Thread {thread_id} finished.")

def run_rlock_threads(num_threads, size):
    """Create and manage threads using RLock for synchronized access."""
    out_list = []
    rlock = threading.RLock()
    threads = []

    # Create all worker threads
    for i in range(num_threads):
        thread = threading.Thread(target=worker, args=(i, size, out_list, rlock))
        threads.append(thread)

    # Start threads with a short delay for readable output
    for thread in threads:
        thread.start()
        time.sleep(0.3)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return out_list

if __name__ == "__main__":
    NUM_THREADS = 3
    SIZE = 7

    final_output = run_rlock_threads(NUM_THREADS, SIZE)

    print("\nFinal Output List:", final_output)
    print(f"Length of list (RLock): {len(final_output)}")
