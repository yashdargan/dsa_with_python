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

    def printing(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=' ')
            tmp = tmp.next
        print()

    def roatation(self, rounds):
        if not self.head or rounds == 0:
            return

        current = self.head
        length = 1
        while current.next:
            current = current.next
            length += 1

        # Making the circular linked list
        current.next = self.head

        # Handle cases where rounds > length of the list
        rounds = rounds % length

        steps_to_new_head = length - rounds
        new_tail = self.head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        self.head = new_tail.next
        new_tail.next = None


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.printing()
    rotate = int(input('enter the number of roatation: '))
    ll.roatation(rotate)
    ll.printing()
