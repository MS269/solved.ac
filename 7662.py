import heapq
import sys


input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())

    min_heap, max_heap = [], []
    keys = [False] * k

    for i in range(k):
        op = list(input().split())

        if op[0] == "I":
            heapq.heappush(min_heap, (int(op[1]), i))
            heapq.heappush(max_heap, (-int(op[1]), i))
            keys[i] = True
        elif op[0] == "D":
            if op[1] == "-1":
                while min_heap and not keys[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    keys[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            elif op[1] == "1":
                while max_heap and not keys[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    keys[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    while min_heap and not keys[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not keys[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
