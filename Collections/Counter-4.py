from collections import Counter, deque

data = ["a", "b", "a", "b", "c", "a"]

print(Counter(data))


q = deque([1, 2, 3])
q.append(4)
q.appendleft(0)

print(q)
