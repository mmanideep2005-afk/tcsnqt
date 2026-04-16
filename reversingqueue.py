'''from collections import deque

q=deque([1,2,3,4,5])
stack=[]
while q:
    stack.append(q.popleft())

while q:
    q.append(stack.pop())

print("reversed queue:",q)'''
class queueusingstacks:
    def _init_(self):
        self.s1=[]#enqueue
        self.s2=[]#dequeue

    def enqueue(self,x):
        self.s1.append(x)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            return"empty"
        
        return self.s2.pop()
        
q= queueusingstacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())