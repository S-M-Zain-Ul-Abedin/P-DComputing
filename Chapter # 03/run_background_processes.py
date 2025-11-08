import multiprocessing
import time
from do_something import do_something

def run_process():
    """Function executed by each process, simulates work and prints status."""
    name = multiprocessing.current_process().name
    print(f"[🚀] Starting {name}")

    # Output list for the process
    out_list = multiprocessing.Manager().list()

    # Different workloads for demonstration
    size = 5 if name == "background_process" else 10
    do_something(size, out_list)

    # Simulate some work delay
    time.sleep(1)
    print(f"[✅] Exiting {name}")

def launch_daemon_demo():
    """Launches a daemon and a non-daemon process to demonstrate behavior."""
    # Daemon process
    bg_proc = multiprocessing.Process(name="background_process", target=run_process)
    bg_proc.daemon = True  # Will exit automatically when main program exits

    # Non-daemon process
    fg_proc = multiprocessing.Process(name="foreground_process", target=run_process)
    fg_proc.daemon = False  # Main program will wait for it

    # Start both processes
    bg_proc.start()
    fg_proc.start()

    # Wait for the foreground process
    fg_proc.join()
    # Optionally join the daemon process with a timeout (it may terminate when main exits)
    bg_proc.join(timeout=2)

if __name__ == "__main__":
    launch_daemon_demo()
