import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def call_api(url):
    """
    ThreadPoolExecutor is a highlevel interface used for parallelizing I/O bound tasks using threads.
    It manages a pool of worker threads which executes the submitted task asynchronously
    """
    # time.sleep(1) # to simulate I/O delay (e.g network call)
    return {"result": f"{url} called"}


if __name__ == "__main__":
    start_time = time.time()
    urls = ["www.test.com/1",
            "www.test.com/2",
            "www.test.com/3",
            "www.test.com/4"]
    # executor = ThreadPoolExecutor(12)  # creates 12 workers
    # futures = []
    # for url in urls:
    #     future = executor.submit(call_api, url)
    #     futures.append(future)
    #     # result = call_api(url)
    #     # print(result)
    #
    # for future in futures:
    #     print(future.result())

    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = [executor.submit(call_api, url) for url in urls]

        for future in as_completed(futures):
            print(future.result())
    elapsed = time.time() - start_time
    print(f"Elapsed: {elapsed:.2f}s")
# ThreadPoolExecutor(max_workers=4): Creates a pool with 4 threads.
# executor.submit(...): Schedules a function to run on a thread.
# as_completed(futures): Returns results as tasks finish (not in order).
# Python threads don’t run in true parallel due to the Global Interpreter Lock (GIL). it switches the context fast which gives illusion of
# parallelism But for I/O-bound tasks, threads can yield control while waiting, making multithreading very effective.


