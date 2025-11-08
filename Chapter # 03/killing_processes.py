import multiprocessing
import time
from do_something import do_something  # Ensure this module exists

def run_task():
    """Function executed in a separate process."""
    manager = multiprocessing.Manager()
    out_list = manager.list()  # Shared list across processes
    print("[🚀] Task started")
    do_something(10, out_list)
    print(f"[✅] Task finished with {len(out_list)} results")

def monitor_process(proc):
    """Monitors process state from start to termination."""
    print("[🔍] Before start:", proc, proc.is_alive())

    proc.start()
    print("[⚙️] Running:", proc, proc.is_alive())

    # Allow process to run for a short while
    time.sleep(2)

    # Terminate and join process
    proc.terminate()
    print("[🛑] Terminated:", proc, proc.is_alive())

    proc.join()
    print("[🔚] Joined:", proc, proc.is_alive())
    print("[📦] Exit code:", proc.exitcode)

if __name__ == "__main__":
    process = multiprocessing.Process(target=run_task)
    monitor_process(process)
