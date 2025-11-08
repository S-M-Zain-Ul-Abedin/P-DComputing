import multiprocessing
import time
from do_something import do_something  # Ensure this file exists

def launch_processes(size):
    """Launches two processes running do_something() in parallel."""
    manager = multiprocessing.Manager()
    out_list1 = manager.list()
    out_list2 = manager.list()

    # Define two independent processes
    p1 = multiprocessing.Process(
        name="Worker-1",
        target=do_something,
        args=(size, out_list1)
    )
    p2 = multiprocessing.Process(
        name="Worker-2",
        target=do_something,
        args=(size, out_list2)
    )

    start = time.time()

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()

    end = time.time()

    # Return results and duration
    return out_list1, out_list2, end - start

if __name__ == "__main__":
    SIZE = 1000
    list1, list2, duration = launch_processes(SIZE)

    print(f"Worker-1 output length: {len(list1)}")
    print(f"Worker-2 output length: {len(list2)}")
    print(f"Execution time: {duration:.2f} seconds")
