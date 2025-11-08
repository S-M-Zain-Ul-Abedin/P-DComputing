import math

def do_something(size, out_list):
    """Performs a simple computation and appends results to the shared list."""
    results = [math.sqrt(i) ** 2 for i in range(size)]
    out_list.extend(results)
