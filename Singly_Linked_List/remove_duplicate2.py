#unsorted
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
        while(temp1 != None):
            temp2 = temp1
            while(temp2.next != None):
                if(temp1.data == temp2.next.data):
                    temp2.next = temp2.next.next
                else:
                    temp2 = temp2.next
            temp1 = temp1.next

    def printlist(self):
        temp = self.head
        while(temp != None):
            print(temp.data,end=" ")
            temp = temp.next



if __name__ == '__main__':
    llist = linkedlist()
    llist.insert(10)
    llist.insert(11)
    llist.insert(12)
    llist.insert(10)
    llist.insert(13)
    llist.insert(12)

    print("Before: ",end=" ")
    llist.printlist()
    llist.removeduplicate()
    print("\nAfter: ",end = " ")
    llist.printlist()