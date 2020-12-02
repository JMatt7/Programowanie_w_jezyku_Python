#!/usr/bin/python
#without the deadlock
import threading
import time
import random

class Operator:

    def __init__(self, initial):
        self.lock = threading.Condition(threading.Lock())
        self.value = initial

    def on(self):
        with self.lock:
            self.value += 1
            self.lock.notify()
    
    def off(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1


class Fork:
    
    def __init__(self, number):
        self.number = number
        self.philosopher = -1
        self.lock = threading.Condition(threading.Lock())
        self.taken = False

    def used(self, philosopher):
        with self.lock:
            while self.taken:
                self.lock.wait()
            self.philosopher = philosopher
            self.taken = True
            self.lock.notifyAll()

    def unused(self, philosopher):
        with self.lock:
            while not self.taken:
                self.lock.wait()
            self.user = -1
            self.taken = False
            self.lock.notifyAll()

class Philosopher(threading.Thread):

    def __init__(self, left_fork: Fork, right_fork: Fork, philosopher_id: int, lock):
        threading.Thread.__init__(self)
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.philosopher_id = philosopher_id
        self.lock = lock

    def do_action(self, action: str):
        print("Philospher number: ", self.philosopher_id , " " , action)
        time.sleep(random.randint(1, 5))

    def run(self):
        self.do_action(str(time.time()) + ": Thinking")
        while True:
            self.lock.off()
            self.do_action(str(time.time()) + ": Picked up left fork")
            self.left_fork.used(self.philosopher_id)
            self.do_action(str(time.time()) + ": Picked up right fork - eating")
            self.right_fork.used(self.philosopher_id)
            self.do_action(str(time.time()) + ": Put down right fork")
            self.right_fork.unused(self.philosopher_id)
            self.do_action(str(time.time()) + ": Put down left fork. Back to thinking")
            self.left_fork.unused(self.philosopher_id)
            self.lock.on()
            
            

if __name__ == "__main__":
    print("start")
    n = 5
    lock = Operator(n-1)
    philosophers = []
    forks = []

    for i in range(n):
        forks.append(Fork(i))
    
    for i in range(n):
        l_fork = forks[i]
        r_fork = forks[(i+1)%5]

        if(i == n-1):
            p = Philosopher(r_fork, l_fork, i+1, lock)
        else:
            p = Philosopher(l_fork, r_fork, i+1, lock)
        p.start()
        philosophers.append(p)
    
    for t in philosophers:
        t.join()

    print("end")
