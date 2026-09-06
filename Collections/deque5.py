from collections import deque

q = deque([1,2,3,4])

q.append(5)
q.appendleft(0)

print(q)
