import threading
import time
from do_something import do_something

def worker(thread_id, size, out_list, condition):
    print(f"🧵 Thread {thread_id} started.")
    do_something(size, out_list)
    with condition:
        print(f"🧵 Thread {thread_id} notifying condition.")
        condition.notify_all()  # notify all waiting threads
    print(f"🧵 Thread {thread_id} finished.")

def monitor(out_list, condition, total_expected):
    with condition:
        while len(out_list) < total_expected:
            condition.wait()
            print(f"👀 Monitor: Current progress = {len(out_list)}/{total_expected}")
    print("✅ Monitor: All items have been added!")

def main():
    out_list = []
    condition = threading.Condition()
    num_threads = 3
    size = 7
    total_expected = num_threads * size

    threads = [
        threading.Thread(target=worker, args=(i, size, out_list, condition))
        for i in range(num_threads)
    ]

    monitor_thread = threading.Thread(target=monitor, args=(out_list, condition, total_expected))

    monitor_thread.start()
    for t in threads:
        t.start()
        time.sleep(0.3)  # shorter delay, smoother thread start

    for t in threads:
        t.join()
    monitor_thread.join()

    print("\n📋 Final Output List:", out_list)
    print(f"✅ Total length: {len(out_list)} (expected {total_expected})")

if __name__ == "__main__":
    main()
