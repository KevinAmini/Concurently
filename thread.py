import threading

def function_1():
    for i in range(10):
        print("t1:" ,i)
        print("\n")

def function_2():
    for j in range(10):
        print("t2:",j)

thread1 = threading.Thread(target=function_1)
thread2 = threading.Thread(target=function_2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()