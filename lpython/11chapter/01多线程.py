import threading

total = 0

def add():
    global total
    for i in range(1000000):
        total += 1


def desc():
    global total
    for i in range(1000000):
        total -= 1


threading1 = threading.Thread(target=add)
threading2 = threading.Thread(target=desc)
threading1.start()
threading2.start()


threading1.join()
threading2.join()


print("total:", total)




