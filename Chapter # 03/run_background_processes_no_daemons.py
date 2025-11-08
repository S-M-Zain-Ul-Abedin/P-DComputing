import multiprocessing
import time
from do_something import do_something

def foo():
    """Function executed by each process."""
    name = multiprocessing.current_process().name
    print(f"Starting {name}\n")

    if name == 'background_process':
        # Simulate a small task without do_something
        for i in range(5):
            print(f'---> {i}\n')
        time.sleep(1)
    else:
        # Simulate a different task using do_something
        results = []
        do_something(3, results)   # ✅ proper argument passing
        print(f"Results from do_something(): {results}")
        time.sleep(1)

    print(f"Exiting {name}\n")

if __name__ == '__main__':
    # Create non-daemon background process
    background_process = multiprocessing.Process(
        name='background_process', target=foo)
    background_process.daemon = False

    # Create another non-daemon process
    NO_background_process = multiprocessing.Process(
        name='NO_background_process', target=foo)
    NO_background_process.daemon = False

    # Start both processes
    background_process.start()
    NO_background_process.start()

    # Wait for both to finish
    background_process.join()
    NO_background_process.join()
