import queue

def task(name, work_queue):
    if work_queue.empty():
        print(f"Task {name} nothingto do")
    else:
        while not work_queue.empty():
            count = work_queue.get()
            total = 0
            print(f"Task {name} running")
            for x in range (count):
                total += 1
            print(f"Task {name} total:{total}")
def main():

    work_queue =queue.Queue()

    for work in [15, 10, 5, 2]:
        work_queue.put(work)