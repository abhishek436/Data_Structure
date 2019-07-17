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

    def seggregate_evenodd(self):
        evenhead = oddhead = evenlast = oddlast = None
        curr = self.head
        while(curr is not None):
            if(curr.data%2 == 0):
                if(evenhead is None):
                    evenhead = evenlast = curr
                    curr = curr.next
                else:
                    evenlast.next = curr
                    evenlast = curr
                    curr = curr.next
            else:
                if (oddhead is None):
                    oddhead = oddlast = curr
                    curr = curr.next
                else:
                    oddlast.next = curr
                    oddlast = curr
                    curr = curr.next

        if(evenhead != None):
            self.head = evenhead
        if(evenhead != None):
            evenlast.next = oddhead
        if(oddhead != None):
            oddlast.next = None







    def printlist(self):
        temp = self.head
        while(temp != None):
            print(temp.data,end=" ")
            temp = temp.next



if __name__ == '__main__':
    llist = linkedlist()
    llist.insert(1)
    llist.insert(2)
    llist.insert(4)
    llist.insert(3)
    llist.insert(6)
    llist.insert(8)

    print("Before: ",end=" ")
    llist.printlist()

    llist.seggregate_evenodd()
    print("\nAfter: ",end = " ")
    llist.printlist()