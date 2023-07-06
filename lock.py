import threading

class Multilock:
    def __init__(self, size):
        self.locks = [threading.Lock() for _ in range(size)]
    
    def acquire(self, process_id):
        self.locks[process_id].acquire()
    
    def release(self, process_id):
        self.locks[process_id].release()
    
    def get_queue(self):
        return [lock.locked() for lock in self.locks]


class MultilockWithTimeout:
    def __init__(self, size):
        self.locks = [threading.Lock() for _ in range(size)]
        self.timeout_grant_in_nsecs = 8000000000
  
    def acquire(self, process_id):
        lock = self.locks[process_id]
        if not lock.acquire(timeout=self.timeout_grant_in_nsecs):
            raise TimeoutError("Timeout occurred while acquiring the lock.")
    
    def release(self, process_id):
        self.locks[process_id].release()
