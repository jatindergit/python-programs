import time
import multiprocessing


def cal_cube(numbers):
    for n in numbers:
        time.sleep(20)
        print("Cube: " , n*n*n)

def cal_square(numbers):
    for n in numbers:
        time.sleep(20)
        print("Square:", n*n)



if __name__ == '__main__':
    numbers = [2, 3, 4, 5, 6]
    print(__name__)
    p1 = multiprocessing.Process(target=cal_cube, args=(numbers,))
    p2 = multiprocessing.Process(target=cal_square, args=(numbers,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

