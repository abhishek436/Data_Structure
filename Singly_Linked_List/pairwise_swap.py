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

    def pairwise_swapnode(self):
        p = self.head
        self.head = p.next
        while(True):
            q = p.next
            temp = q.next
            q.next = p
            if(temp is None or temp.next is None):
                p.next = None
                break
            else:
                p.next = temp.next
                p = temp




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

    llist.pairwise_swapnode()
    print("\nAfter: ",end = " ")
    llist.printlist()