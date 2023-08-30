from queue import Queue
Q = Queue(maxsize = 4)

print(Q.empty())
Q.put(2)
Q.put(3)

x = Q.get()
print (x)

print(Q.full())
