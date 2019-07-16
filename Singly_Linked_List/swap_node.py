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

    def swapnode(self,x,y):

        if(x == y):
            return
        prevx = None
        temp1 = self.head
        while(temp1 != None):
            if(temp1.data == x):
                break
            else:
                prevx = temp1
                temp1 = temp1.next

        prevy = None
        temp2 = self.head
        while (temp2 != None):
            if (temp2.data == y):
                break
            else:
                prevy = temp2
                temp2 = temp2.next

        if(temp1 == None and temp2 == None):
            return

        if(prevx != None):
            prevx.next = temp2
        else:
            self.head = temp2

        if (prevy != None):
            prevy.next = temp1
        else:
            self.head = temp1

        temp = temp1.next
        temp1.next = temp2.next
        temp2.next = temp



    def printlist(self):
        temp = self.head
        while(temp != None):
            print(temp.data,end=" ")
            temp = temp.next



if __name__ == '__main__':
    llist = linkedlist()
    llist.insert(10)
    llist.insert(15)
    llist.insert(12)
    llist.insert(13)
    llist.insert(20)
    llist.insert(14)

    print("Before: ",end=" ")
    llist.printlist()

    llist.swapnode(10,20)
    print("\nAfter: ",end = " ")
    llist.printlist()