import threading
import time

class SharedList:
    def __init__(self):
        self.data = []

        self.searcher_count = 0

        # Semaphores
        self.search_mutex = threading.Semaphore(1)
        self.insert_mutex = threading.Semaphore(1)
        self.no_searchers = threading.Semaphore(1)
        self.list_mutex = threading.Semaphore(1)


    def search(self, value):
        # Entry section
        self.search_mutex.acquire()
        self.searcher_count += 1
        if self.searcher_count == 1:
            self.no_searchers.acquire()   # block deleter
        self.search_mutex.release()

        # Critical section (search)
        print(f"Searching for {value}")
        found = value in self.data
        time.sleep(1)

        # Exit section
        self.search_mutex.acquire()
        self.searcher_count -= 1
        if self.searcher_count == 0:
            self.no_searchers.release()   # allow deleter
        self.search_mutex.release()

        return found


    def insert(self, value):
        self.insert_mutex.acquire()

        print(f"Inserting {value}")
        self.data.append(value)
        time.sleep(1)

        self.insert_mutex.release()


    def delete(self, value):
        # Full exclusivity
        self.list_mutex.acquire()
        self.no_searchers.acquire()
        self.insert_mutex.acquire()

        print(f"Deleting {value}")
        if value in self.data:
            self.data.remove(value)
        time.sleep(1)

        self.insert_mutex.release()
        self.no_searchers.release()
        self.list_mutex.release()

# Using three semaphores to manage access:
# search_mutex     # protects searcher_count
# insert_mutex     # ensures only one inserter
# no_searchers     # blocks deleter if searchers exist
# list_mutex       # gives deleter full exclusive access


if __name__ == "__main__":
    shared_list = SharedList()
    threads = [
    threading.Thread(target=shared_list.insert, args=(1,)),
    threading.Thread(target=shared_list.search, args=(1,)),
    threading.Thread(target=shared_list.search, args=(2,)),
    threading.Thread(target=shared_list.delete, args=(1,))
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()
