import threading
exitFlag=0


class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.counter=counter

    def run(self):
        while self.counter <= 10:
            if exitFlag:
                self.name.exit()
            if(self.counter!=0):
                print(self.name+" : "+str(self.counter)+"\n")
            self.counter+=2


t2=myThread(1,"Thread-1",1)
t1=myThread(2,"Thread-2",1)


t2.start()
t1.start()

t2.join()
t1.join()