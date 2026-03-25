import time
from concurrent.futures import ProcessPoolExecutor


def cpu_bound_task(n):
    """
    simulate a CPU-intensive task, like calculating factorial or performing a large sum.
    """
    print(f"Calculating sum for {n}")
    total = sum(i * i for i in range(n))
    return f"Done for {n}, result: {total}"


if __name__ == "__main__":
    numbers = [10_000_000, 20_000_000, 30_000_000, 40_000_000]

    start = time.time()

    with ProcessPoolExecutor() as executor:
        results = executor.map(cpu_bound_task, numbers)

    for res in results:
        print(res)

    print(f"Time taken: {time.time() - start:.2f} seconds")
# The concurrent.futures.ProcessPoolExecutor is part of Python's multiprocessing capabilities.'
# It spins up separate processes, each with its own Python interpreter and memory space, so it bypasses the Global Interpreter Lock (GIL).
# This line: results = executor.map(cpu_bound_task, numbers)
# Submits the cpu_bound_task() function for each item in the numbers list.
# Executes those calls in parallel using worker processes (or threads).

# Returns a lazy iterator (results) of results, in the same order as the input iterable ( numbers ).
# Each call becomes:
# cpu_bound_task(10_000_000)
# cpu_bound_task(20_000_000)
# cpu_bound_task(30_000_000)
# cpu_bound_task(40_000_000)
# And all are run concurrently by different processes.
# Orders Guarantee: Even though tasks run in parallel, executor.map() guarantees that the results are returned in the order of the input list






