class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_value):
        new_node = Node(new_value)
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def printing(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()
    ''' 
    using two pointer approch:
    moving middle pointer if current pointer travels twice of distance,
    eventually middle will comes at middle , current will be at end
    Example-> its like 2 race car travels, one with 2x speed of other,
    first car completes race, but other one was at middle of track
    '''
    # Find Middle of the Linked List by Counting Nodes (One-pass):

    def findingMiddle(self):
        middle = self.head
        current = self.head
        length = 1
        while current:
            if length % 2 == 0:
                middle = middle.next
            current = current.next
            length += 1
        print(middle.value)


if __name__ == "__main__":
    ll = LinkList()
    ll.append(3)
    ll.append(4)
    ll.append("ggg")
    ll.append(45)
    ll.append("ree")
    ll.printing()
    ll.findingMiddle()
