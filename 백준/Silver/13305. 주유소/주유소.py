import sys
input = sys.stdin.readline

N = int(input())
dists = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_cost = prices[0] * dists[0]
min_price = prices[0]

for index in range(1, N - 1):
    if min_price > prices[index]:
        min_price = prices[index]
    min_cost += min_price * dists[index]

print (min_cost)
