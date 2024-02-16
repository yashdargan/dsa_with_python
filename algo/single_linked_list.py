class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None

class Sll:
    def __init__(self):
        self.head = None
     
    def traversal(self):
        if self.head is None:
            print("empty linked list")
        else :
            a = self.head
            while a is not None:
                print(a.data,end =" ")
                a=a.next
    

    def insertion_at_begining(self,data):
        nb  = Node(data)
        nb.next = self.head
        self.head = nb


    def insertion_at_end(self,data):
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
         
        a.next = ne 
        
    def insertion_at_specific(self,data,postion):
        ns = Node(data)
        a = self.head
        for i in range(1,postion-1):
            a = a.next
        
        ns.next = a.next
        a.next = ns
    
    def deletion_at_begining(self):
        a = self.head
        self.head = a.next
        a.next = None
     
    def deletion_at_end(self):
        p = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            p = p.next
        p.next = None
    
    def deletion_at_specific(self,position):
        p = self.head
        a = self.head.next
        for i in range(1,position-1):
            a = a.next
            p =p.next
        p.next = a.next
        a.next = None



n1 = Node(5)#node creation
sll = Sll()# calling single linked list function
sll.head = n1# setting head at node 1
n2 = Node(10)#creating other nodes
n1.next = n2#linking node1 to node 2
n3 = Node(15)
n2.next = n3
n4 = Node(20)
n3.next = n4

#insertion opertion
#sll.insertion_at_begining(2)
#sll.insertion_at_end(25)
#sll.insertion_at_specific(12,4)

#deletion opertion
#sll.deletion_at_begining()
#sll.deletion_at_end()
#sll.deletion_at_specific(2)

sll.traversal()
