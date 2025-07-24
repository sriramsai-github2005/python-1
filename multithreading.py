import threading

def square(numbers):
    print("calc square")
    for n in numbers:
        print(n*n)

def cube(numbers):
    print("calc cube")
    for n in numbers:
        print(n*n*n)

arr = [2, 4, 6, 8]

t1 = threading.Thread(target=square, args=(arr,))
t2 = threading.Thread(target=cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

