class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.queue = [None]*size
        self.front = -1
        self.rear = -1
    
    def Isfull(self):
        return (self.rear+1)%self.size == self.front
    def Isempty(self):
        return self.front == -1
    def enqueue(self,data):
        if self.Isfull():
            print("Queue is full")
            return
        if self.Isempty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear+1)%self.size
        
        self.queue[self.rear]= data
        print(f"Inserted :{data}")
    
    def dequeue(self):
        if self.Isempty():
            print("Queue is empty")
            return
        return self.queue[self.front]
    def display(self):
        if self.Isempty():
            print("Queue is empty")
            return
        print("Queue element :",end=" ")
        i = self.front
        while True:
            print(self.queue[i],end=" ")
            if i == self.rear:
                break
            i = (i+1)%self.size
        print()
clq= CircularQueue(5)
clq.enqueue(10)
clq.enqueue(20)
clq.enqueue(30)