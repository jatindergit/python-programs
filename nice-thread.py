import threading
import time


def sleeper(seconds, name):
    print("Hi, I am going to sleep for {} seconds".format(seconds))
    time.sleep(seconds)
    print("{} has woken up from sleep!!!".format(name))


thread1 = threading.Thread(target=sleeper, args=(5, 'Thread 1'))
thread1.start()


