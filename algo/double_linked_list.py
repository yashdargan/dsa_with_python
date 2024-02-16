class Node: 
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class Dll:
    def __init__(self):
        self.head = None

    def forward_traversal(self):
        if self.head is None:
            print("empty linked list")
        
        else:
            a = self.head
            while a is not None:
                print(a.data,end=" ")
                a = a.next
    
    def backward_traversal(self):
        print(" ")
        a = self.head
        
        while a.next is not None:
            a  = a.next
        
        while a is not None:
            print(a.data,end=" ")
            a = a.prev
            
    def insertion_at_begining(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head.prev = nb
        self.head = nb
    
    def insertion_at_end(self,data):
        ne =Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        
        a.next = ne 
        ne.prev = a
     
    def insertion_at_specific(self,data,position):
        ns =  Node(data)
        a =self.head
        for i in range(1,position-1):
            a = a.next
        ns.next = a.next
        a.next.prev = ns
        a.next = ns
        ns.prev = a 
    
    def deletion_at_begining(self):
        a = self.head
        self.head = a.next
        a.next.prev = None
        a.next =None

    def deletion_at_end(self):
        a = self.head.next
        p = self.head
        while a.next is not None:
            a = a.next
            p =p.next
        
        p.next = None
        a.prev = None
    
    def deletion_at_specific(self,position):
        a = self.head.next
        p =self.head
        for i in range(1,position-1):
            a =a.next
            p=p.next
        
        p.next = a.next
        a.next.prev = p
        a.next =None
        a.prev = None



n1 = Node(5)
dll =Dll()
dll.head = n1
n2 = Node(10)
n1.next = n2
n2.prev = n1
n3 = Node(15)
n2.next = n3
n3.prev = n2
n4 = Node(20)
n3.next = n4
n4.prev = n3

#insertion opertion
#dll.insertion_at_begining(2)
#dll.insertion_at_end(25)
#dll.insertion_at_specific(12,4)

#deletion operation
#dll.deletion_at_begining()
#dll.deletion_at_end()
#dll.deletion_at_specific(3)

dll.forward_traversal()
dll.backward_traversal()
