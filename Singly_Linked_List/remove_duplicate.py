class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
            return

        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node

    def removeduplicate(self):
        temp1 = self.head
        while(temp1.next != None):
            if(temp1.data == temp1.next.data):
                temp1.next = temp1.next.next
            else:
                temp1 = temp1.next

    def printlist(self):
        temp = self.head
        while(temp != None):
            print(temp.data,end=" ")
            temp = temp.next


if __name__ == '__main__':
    llist = linkedlist()
    llist.insert(1)
    llist.insert(2)
    llist.insert(2)
    llist.insert(3)
    llist.insert(3)

    print("Before: ",end=" ")
    llist.printlist()
    llist.removeduplicate()
    print("\nAfter: ",end = " ")
    llist.printlist()