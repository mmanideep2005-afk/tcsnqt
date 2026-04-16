class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class CircularLL:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        
        new_node.next = self.head
        temp.next = new_node
        self.head = new_node
    

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head
    

    def insert_at_pos(self, pos, data):
        if pos == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        temp = self.head

        for _ in range(pos - 1):
            temp = temp.next
            if temp == self.head:
                return
        
        new_node.next = temp.next
        temp.next = new_node


    def delete_begin(self):
        if self.head is None:
            return
        
        if self.head.next == self.head:
            self.head = None
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = self.head.next
        self.head = self.head.next
    

    def delete_end(self):
        if self.head is None:
            return
        
        if self.head.next == self.head:
            self.head = None
            return
        
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head
    

    def delete_value(self, key):
        if self.head is None:
            return
        
        if self.head.data == key:
            self.delete_begin()
            return
        
        temp = self.head
        while temp.next != self.head:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next
    

    def search(self, key):
        if self.head is None:
            return False
        
        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        
        return False

    
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")



cll = CircularLL()

cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)

cll.display()

cll.insert_at_beginning(5)
cll.display()

cll.delete_end()
cll.display()

print(cll.search(20))  # True
print(cll.search(100)) # False