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
            while(temp.next is not None):
                temp = temp.next
            temp.next = new_node


    def sum_of_num(self,num1,num2):
        sumnode = None
        temp = None
        c = 0
        while(num1 is not None or num2 is not None):
            if(num1 == None):
                f = 0
            else:
                f = num1.data

            if(num2 == None):
                s = 0
            else:
                s = num2.data

            sum = f+s+c
            c = 1 if sum >= 10 else 0
            sum = sum if sum < 10 else sum%10

            sumnode = Node(sum)

            if self.head is None:
                self.head = sumnode
            else:
                temp.next = sumnode

            temp = sumnode

            if num1 is not None:
                num1 = num1.next
            if num2 is not None:
                num2 = num2.next


        if(c > 0):
            sumnode.next = Node(c)

    def print(self):
        temp = self.head
        while (temp != None):
            print(temp.data, end=" ")
            temp = temp.next



if __name__ == '__main__':
    num1 = linkedlist()
    num2 = linkedlist()

    num1.insert(5)
    num1.insert(6)
    num1.insert(3)
    num2.insert(8)
    num2.insert(4)
    num2.insert(2)

    print("num1: ", end=" ")
    num1.print()

    print("\nnum2: ", end=" ")
    num2.print()

    res = linkedlist()
    res.sum_of_num(num1.head,num2.head)
    print("\nSum: ", end=" ")
    res.print()