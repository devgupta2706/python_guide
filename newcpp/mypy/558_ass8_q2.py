import threading
exitFlag=0


class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter

    def run(self):
        lock.acquire()
        while self.counter <= 100:
            if exitFlag:
                self.name.exit()
            if(self.counter!=0):
                print(self.counter)
            self.counter+=2
        lock.release()

lock=threading.Lock()

#t1=myThread(1,"Thread-1",1)
t2=myThread(2,"Thread-2",0)


#t1.start()
t2.start()

#t1.join()
t2.join()