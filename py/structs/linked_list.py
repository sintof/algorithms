from utils.speed import timeit


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


    def __repr__(self):
        s = ""
        current = self
        while current:
            s += str(current.data) + " "
            current = current.next
        return s


@timeit
def insert_end(head, data):
    current = head
    while current.next:
        current = current.next
    current.next = Node(data)

    return head


@timeit
def delete_node(head, key):
    current = head
    previous = None
    while current:
        if current.data == key:
            if previous:
                previous.next = current.next
            else:
                head = current.next
        previous = current
        current = current.next
    return head





head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8))))))))
# head = Node(1)


def start():
    global head
    print(head)

    head = insert_end(head, 9)
    print(head)

    head = delete_node(head, 9)
    print(head)