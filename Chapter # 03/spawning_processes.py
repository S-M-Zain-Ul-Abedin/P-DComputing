import multiprocessing
from do_something import do_something

def run_task(index):
    """Function executed by each process."""
    print(f"[⚙️] Process {index} started")
    out_list = multiprocessing.Manager().list()
    do_something(index * 1000, out_list)
    print(f"[✅] Process {index} finished with {len(out_list)} results")

def launch_processes():
    """Launch multiple processes concurrently."""
    processes = []

    # Create and start all processes
    for i in range(6):
        proc = multiprocessing.Process(target=run_task, args=(i,))
        processes.append(proc)
        proc.start()

    # Wait for all processes to finish
    for proc in processes:
        proc.join()

if __name__ == "__main__":
    launch_processes()
