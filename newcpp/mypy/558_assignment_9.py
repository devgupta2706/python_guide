import threading
import random
exitFlag = 0


class myThread1(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        lock.acquire()
        print(self.name),
        print(self.threadID)
        lock.release()


class myThread2(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        lock.acquire()
        print(self.name),
        print(self.threadID)
        lock.release()


lock = threading.Lock()
n = 0
# This is the queue of natural numbers shown by the following threads 1 and 2.
while(n <= 10):
    i = random.randint(0,1)
    if(i == 0):
        t1 = myThread1(n, "Thread-1")
        t1.start()
        t1.join()
    else:
        t2 = myThread2(n, "Thread-2")
        t2.start()
        t2.join()
    n += 1
