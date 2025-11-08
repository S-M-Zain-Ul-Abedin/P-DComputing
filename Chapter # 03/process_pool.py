import multiprocessing
from do_something import do_something  # Ensure this file exists

def compute_square(data):
    """Compute the square of a number, simulating extra work."""
    temp = []
    do_something(2, temp)  # Simulate a small workload
    return data * data

def run_pool(inputs, num_processes):
    """Run computations in parallel using a process pool."""
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(compute_square, inputs)
    return results

if __name__ == "__main__":
    INPUTS = list(range(10))
    NUM_PROCESSES = 4

    output = run_pool(INPUTS, NUM_PROCESSES)
    print("Pool:", output)
