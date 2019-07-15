# reverse using recursion
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node

    def reverse(self,p):
        if(p.next is None):
            self.head = p
            return
        else:
            q = Node(None)
            self.reverse(p.next)
            q = p.next
            q.next = p
            p.next = None

    def printlist(self):
        temp = self.head
        print("List : ", end=" ")
        while(temp != None):
            print(temp.data,end= " ")
            temp = temp.next

if __name__=='__main__':
    llist = linkedlist()
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)

    print("\nBefore Reverse ")
    llist.printlist()
    print("\nAfter Reverse ")
    llist.reverse(llist.head)
    llist.printlist()

