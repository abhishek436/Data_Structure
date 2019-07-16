class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head1 = None
        self.head2 = None

    def insert(self,data):
        new_node = Node(data)
        if(self.head1 is None):
            self.head1 = new_node
            return

        else:
            temp = self.head1
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node

    def reverse(self,p):
        temp1 = p
        prev = None
        temp2 = Node(None)

        while(temp1 != None):
            temp2 = temp1.next
            temp1.next = prev
            prev = temp1
            temp1 = temp2
        self.head2 = prev
        return self.head2

    def checkpalindrome(self):
        p = self.head1
        q = self.head1
        sec_start = None

        while(True):
            p = p.next.next
            if(p is None):
                sec_start = q.next
                break

            if(p.next is None):
                sec_start = q.next.next
                break

            q = q.next

        q.next = None  #sepreating first half and second half

        sec_start = self.reverse(sec_start) # reversing second half
        fir_start = self.head1

        # temp1 = sec_start
        # while(temp1 != None):
        #     print(temp1.data)
        #     temp1 = temp1.next
        #
        # temp2 = fir_start
        # while (temp2 != None):
        #     print(temp2.data)
        #     temp2 = temp2.next


        while(fir_start != None and sec_start != None):
            if(fir_start.data == sec_start.data):
                fir_start = fir_start.next
                sec_start = sec_start.next
            else:
                return False

        return True





    def printlist(self):
        temp = self.head1
        while(temp != None):
            print(temp.data,end=" ")
            temp = temp.next


if __name__ == '__main__':
    llist = linkedlist()
    llist.insert('R')
    llist.insert('A')
    llist.insert('M')
    llist.insert('A')
    llist.insert('R')

    if(llist.checkpalindrome() is True):
        print("Palindrome")
    else:
        print("Not Palindrome")

