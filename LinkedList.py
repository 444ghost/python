class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution: 
    def display(self, head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def delete(self, head):

        current = head
        while current.next:
            previous = current
            current = current.next
            print("delete")
        head = previous
        head.next = None

    def insert(self, head, data):
    #Complete this method

        n = Node(data)
        if head:
            # print("if head:")
            current = head
            while current.next:
                current = current.next
                # print("loop")
            current.next = n
            return head
        else:
            # print("else:")
            return n

mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.delete(head)
mylist.display(head); 	  