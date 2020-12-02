#!/usr/bin/env python
import random
import threading
import plotille
result = {}

def sub_histogram(start, end, data, lock, thread_id):
    sub_result = {}

    for x in data[start:end]:
        if not int(x) in sub_result:
            sub_result[int(x)] = 1
        else:
            sub_result[int(x)] += 1
    lock.acquire()
    for key in sub_result:
        if key in result:
            result[key] += sub_result[key]
        else:
            result[key] = sub_result[key]
    lock.release()



if __name__ == "__main__":
    lower_bound = 0
    upper_bound = 100
    numbers = 1000
    data =[lower_bound + random.random()*upper_bound for i in range(numbers)]
    threads = 4
    threads_array = []
    sub_part = int(numbers/threads)
    threadLock = threading.Lock()
    
    for i in range(threads):
        t = threading.Thread(target=sub_histogram, args=(0 + i*sub_part, sub_part + i*sub_part, data, threadLock, i))
        threads_array.append(t)
        t.start()

    for thread in threads_array:
        thread.join()

    temp = 0
    result = dict(sorted(result.items(), key=lambda item: item[0]))
    print(result)
    