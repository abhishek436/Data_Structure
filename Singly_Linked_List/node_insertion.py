class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def insert(self,data,position):
        temp1 = Node(data)
        if(position == 1):
            temp1.next = self.head
            self.head = temp1

        else:
            temp2 = self.head
            for i in range(position-2):
                temp2 = temp2.next
            temp1.next = temp2.next
            temp2.next = temp1


    def delete(self,position):
        temp1 = self.head
        if(position == 1):
            self.head = temp1.next

        else:
            temp2 = Node(None)
            for i in range(position-2):
                temp1 = temp1.next
            temp2 = temp1.next.next
            temp1.next = temp2


    def reverse(self):
        temp1 = self.head
        prev = None
        temp2 = Node(None)

        while(temp1 != None):
            temp2 = temp1.next
            temp1.next = prev
            prev = temp1
            temp1 = temp2
        self.head = prev


    def printlist(self):
        temp = self.head
        print("List : ", end=" ")
        while(temp != None):
            print(temp.data,end= " ")
            temp = temp.next

    def count(self):
        temp = self.head
        c = 0
        while(temp != None):
            temp = temp.next
            c = c+1
        return c


if __name__=='__main__':
    llist = LinkedList()
    while(True):
        print("\n1. Insert\n2. Delete\n3. Print\n4. Reverse\n5. Exit")
        n = int(input("Enter the Choice: "))
        if(n == 1):
            num = int(input("\nEnter the number :"))
            pos = int(input("Enter the position :"))
            while(pos > llist.count()+1):
                print("please enter right position to insert node")
                pos = int(input("Enter the position :"))
            llist.insert(num,pos)
            llist.printlist()

        elif(n == 2):
            pos = int(input("Enter the position: "))
            while(pos > llist.count() + 1):
                print("please enter right position to delete node")
                pos = int(input("Enter the position :"))
            llist.delete(pos)
            llist.printlist()

        elif(n == 3):
            llist.printlist()

        elif(n == 4):
            llist.reverse()
            llist.printlist()

        elif(n == 5):
            break

        else:
            print("Please enter right choice")

