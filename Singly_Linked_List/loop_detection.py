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


    def detectloop(self):
        slow = self.head
        fast = self.head
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True

if __name__ == '__main__':
    llist = linkedlist()
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    llist.insert(5)

    llist.head.next.next.next.next = llist.head

    if(llist.detectloop() == True):
        print("loop detected")
    else:
        print("loop not found")


