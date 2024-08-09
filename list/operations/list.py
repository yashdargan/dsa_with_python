class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linklist:
    def __init__(self, head=None):
        self.head = head
        # simple insertion of Linklist

    def append(self, new_value):
        new_node = Node(new_value)
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def inserationAtStart(self, new_value):
        new_node = Node(new_value)
        if new_node:
            new_node.next = self.head
            self.head = new_node

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
