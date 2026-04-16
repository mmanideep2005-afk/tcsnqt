# from collections import deque
# dq=deque()
# #inserting elements
# dq.append(10)
# dq.append(20)
# dq.appendleft(5)
# print("deque after insertion:",dq)
# #delete elements
# dq.pop()
# print("after pop:",dq)
# dq.popleft()
# print("after popleft:",dq)
# #add more elements
# dq.append(30)
# dq.append(40)
# print("final deque:",dq)
# #peek
# print("front element:",dq[0])
# print("rear element:",dq[-1])

# #size
# print("size:",len(dq))




# from collections import deque

# def reverse(dq,k):
#     stack=[]

#     for _ in range(k):
#         stack.append(dq.popleft())

#     while stack:
#         dq.append(stack.pop())

#     for _ in range(len(dq) -k):
#         dq.append(dq.popleft())

#     return dq
# dq=deque([1,2,3,4,5])
# k=3

# print("Result:",reverse(dq,k))


from collections import deque

'''def is_palindrome(s):
    dq =deque(s)

    while len(dq)>1:
        if dq.popleft()!=dq.pop():
            return False
    return True
s="madam"
print("palindrome:",is_palindrome(s))'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# traversal functions

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

def main():
    # create nodes
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    # connecting nodes
    root.left = node2
    root.right = node3

    node2.left = node4
    node2.right = node5

    print("\nInorder Traversal:")
    inorder(root)

    print("\nPreorder Traversal:")
    preorder(root)

    print("\nPostorder Traversal:")
    postorder(root)

main()

