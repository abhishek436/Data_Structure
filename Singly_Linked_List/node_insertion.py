class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertBeginning(self,new_data):
        temp = Node(new_data)
        temp.next = self.head
        self.head = temp

    def printlist(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next

if __name__=='__main__':
    llist = LinkedList()
    n = int(input("Enter number of Node: "))
    for i in range(n):
        num = int(input("enter the number :"))
        llist.insertBeginning(num)
        llist.printlist()
