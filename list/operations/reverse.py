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
        tmp = self.head
        while tmp:
            print(tmp.value, end=" ")
            tmp = tmp.next
        print()

    def reverse(self):
        ptr = None
        ftr = self.head
        while ftr:
            curr = ftr.next
            ftr.next = ptr
            ptr = ftr
            ftr = curr
        self.head = ptr


if __name__ == "__main__":
    ll = LinkList()
    ll.append(6)
    ll.append(5)
    ll.append(4)
    ll.append(3)
    ll.append(2)
    ll.printing()
    ll.reverse()
    ll.printing()
