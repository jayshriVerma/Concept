from asyncio import threads
import threading
import time

class SharedList:
    def __init__(self):
        self.data = []

        # Synchronization primitives
        self.searcher_count = 0
        self.searcher_lock = threading.Lock()     # protects searcher_count
        self.no_searchers = threading.Condition(self.searcher_lock)

        self.insert_lock = threading.Lock()       # only one inserter at a time
        self.delete_lock = threading.Lock()       # only one deleter total access

    
    def search(self, value):
        # Register searcher
        with self.searcher_lock:
            self.searcher_count += 1

        # Perform search (can run with other searchers and one inserter)
        print(f"Searching for {value}")
        found = value in self.data
        time.sleep(1)

        # Unregister searcher
        with self.searcher_lock:
            self.searcher_count -= 1
            if self.searcher_count == 0:
                self.no_searchers.notify_all()

        return found

    
    def insert(self, value):
        # Only one inserter at a time
        with self.insert_lock:
            print(f"Inserting {value}")
            self.data.append(value)
            time.sleep(1)

    def delete(self, value):
        # Only one deleter at a time
        with self.delete_lock:

            # Wait until no searchers
            with self.searcher_lock:
                while self.searcher_count > 0:
                    self.no_searchers.wait()

            print(f"Deleting {value}")
            if value in self.data:
                self.data.remove(value)
            time.sleep(1)

if __name__ == "__main__":
    shared_list = SharedList()
    threads = []

    threads.append(threading.Thread(target=shared_list.insert, args=(1,)))
    threads.append(threading.Thread(target=shared_list.search, args=(1,)))
    threads.append(threading.Thread(target=shared_list.search, args=(2,)))
    threads.append(threading.Thread(target=shared_list.delete, args=(1,)))

    
    for t in threads:
        t.start()

    for t in threads:
        t.join()

# This is a classic readers–writers synchronization problem variant with three roles:
# Searchers → like readers (can run together)
# Inserters → special writers (can run with searchers, but not with other inserters)
# Deleters → full writers (must be completely exclusive)