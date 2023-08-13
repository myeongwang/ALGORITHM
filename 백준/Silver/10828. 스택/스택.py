import sys

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return -1
        return self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self):
        return int(not self.items)

    def top(self):
        if not self.items:
            return -1
        return self.items[-1]

N = int(sys.stdin.readline().strip())  # 입력 받기
stack = Stack()

for _ in range(N):
    command = sys.stdin.readline().strip().split()
    if command[0] == "push":
        stack.push(int(command[1]))
    elif command[0] == "pop":
        print(stack.pop())
    elif command[0] == "size":
        print(stack.size())
    elif command[0] == "empty":
        print(stack.empty())
    elif command[0] == "top":
        print(stack.top())