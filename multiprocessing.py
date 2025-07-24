import multiprocessing

def square(numbers):
    print("calc square")
    for n in numbers:
        print(n*n)
def cube(numbers):
    print("calc cube")
    for n in numbers:
        print(n*n*n)

arr = [2, 4, 6, 8]

p1 = multiprocessing.Process(target=square, args=(arr,))
p2 = multiprocessing.Process(target=cube, args=(arr,))


p1.start()
p2.start


p1.join()
p2.join()