#rotate linked list from specific position clockwise
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

    def rotate(self,pos):
        current = self.head
        count = 1
        while(count < pos and current is not None):
            current = current.next
            count = count+1

        breaknode = current

        while(current.next is not None):
            current = current.next

        current.next = self.head

        self.head = breaknode.next

        breaknode.next = None









    def printlist(self):
        temp = self.head
        while(temp != None):
            print(temp.data,end=" ")
            temp = temp.next



if __name__ == '__main__':
    llist = linkedlist()
    llist.insert(10)
    llist.insert(20)
    llist.insert(30)
    llist.insert(40)
    llist.insert(50)
    llist.insert(60)

    print("Before: ",end=" ")
    llist.printlist()

    llist.rotate(4)
    print("\nAfter: ",end = " ")
    llist.printlist()