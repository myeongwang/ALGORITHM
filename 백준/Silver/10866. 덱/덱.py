import sys
from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()
        
    def push_front(self, x):
        self.items.appendleft(x)
        
    def push_back(self, x):
        self.items.append(x)
        
    def pop_front(self):
        if self.items:
            return self.items.popleft()
        else:
            return -1
        
    def pop_back(self):
        if self.items:
            return self.items.pop()
        else:
            return -1
        
    def size(self):
        return len(self.items)
    
    def empty(self):
        return int(not self.items)
    
    def front(self):
        if self.items:
            return self.items[0]
        else:
            return -1
        
    def back(self):
        if self.items:
            return self.items[-1]
        else:
            return -1

N = int(sys.stdin.readline().strip())
deque = Deque()

for _ in range(N):
    command = sys.stdin.readline().strip().split()
    if command[0] == "push_front":
        deque.push_front(int(command[1]))
    elif command[0] == "push_back":
        deque.push_back(int(command[1]))
    elif command[0] == "pop_front":
        print(deque.pop_front())
    elif command[0] == "pop_back":
        print(deque.pop_back())
    elif command[0] == "size":
        print(deque.size())
    elif command[0] == "empty":
        print(deque.empty())
    elif command[0] == "front":
        print(deque.front())
    elif command[0] == "back":
        print(deque.back())