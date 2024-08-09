# initalization of Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# initailization of LinkList class


class Linklist:
    def __init__(self, head=None):
        self.head = head
    # creation and inseration at end of LinkList

    def append(self, new_value):
        new_node = Node(new_value)
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    # inseration at Beginging

    def inserationAtStart(self, new_value):
        new_node = Node(new_value)
        if new_node:
            new_node.next = self.head
            self.head = new_node

    def inserationAtMiddle(self, new_value):
        new_node = Node(new_value)
        if new_node:
            middle = self.head
            curr = self.head.next
            while curr.next and curr:
                middle = middle.next
                curr = curr.next.next
            after = middle.next
            middle.next = new_node
            new_node.next = after

    def deletionATStart(self):
        ptr = self.head.next
        self.head = ptr

    def deletionAtEnd(self):
        ptr = self.head
        utr = None
        while ptr.next:
            utr = ptr
            ptr = ptr.next
        utr.next = None

    def deletionAtMiddle(self):
        ptr = self.head.next
        utr = None
        middle = self.head
        while ptr and ptr.next:
            utr = middle
            middle = middle.next
            ptr = ptr.next.next
        utr.next = middle.next
        middle.next = None
        # printing the value of Linklist

    def Printing(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()


if __name__ == "__main__":
    ll = Linklist()
    ll.append(6)
    ll.append(2)
    ll.append("dog")
    ll.Printing()
    ll.inserationAtStart("cat")
    ll.Printing()
    ll.deletionATStart()
    ll.Printing()
    ll.deletionAtEnd()
    ll.Printing()
    ll.inserationAtMiddle(4)
    ll.Printing()
    ll.deletionAtMiddle()
    ll.Printing()
