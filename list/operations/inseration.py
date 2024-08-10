class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
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

    def swap(self, tmp1, tmp2):
        tmp = tmp2.data
        tmp2.data = tmp1.data
        tmp1.data = tmp

    def inserationSort(self):
        current = self.head
        swaping = True
        while swaping:
            swaping = False
            while current and current.next:
                if current.data > current.next.data:
                    self.swap(current, current.next)
                    swaping = True
                current = current.next
            current = self.head

    def priting(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.next
        print()


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(10)
    ll.append(1)
    ll.append(8)
    ll.priting()
    ll.inserationSort()
    ll.priting()
