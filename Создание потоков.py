import threading
import time


def numbers():
    for i in range(1, 11):
        print(i)
        time.sleep(1)


def letters():
    for j in range(ord('a'), ord('k')):
        print(chr(j))
        time.sleep(1)


num = threading.Thread(target=numbers, args=())
let = threading.Thread(target=letters, args=())

num.start()
let.start()


num.join()
let.join()
print('Потоки выполнены')

