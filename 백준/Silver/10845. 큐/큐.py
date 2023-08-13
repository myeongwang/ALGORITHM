import sys

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return -1
        else:
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def empty(self):
        if not self.items:
            return 1
        else:
            return 0

    def front(self):
        if not self.items:
            return -1
        else:
            return self.items[0]

    def back(self):
        if not self.items:
            return -1
        else:
            return self.items[-1]

N = int(sys.stdin.readline().strip())
queue = Queue()

for _ in range(N):
    command = sys.stdin.readline().strip().split()
    if command[0] == "push":
        queue.push(int(command[1]))
    elif command[0] == "pop":
        print(queue.pop())
    elif command[0] == "size":
        print(queue.size())
    elif command[0] == "empty":
        print(queue.empty())
    elif command[0] == "front":
        print(queue.front())
    elif command[0] == "back":
        print(queue.back())