from utils.speed import timeit


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


    def __repr__(self):
        current = self
        s = ""
        while current:
            s += str(current.data) + " -> "
            current = current.next
        s += "None"
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


@timeit
def search(head, key):
    current = head
    while current:
        if current.data == key:
            return True
        current = current.next
    return False


@timeit
def reverse(head):
    prev = None
    cur = head
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev


@timeit
def detect_loop(head):
    slow = head
    fast = head
    while fast and slow and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


@timeit
def bubble_sort(head):
    cur = head
    while cur:
        runner = cur
        while runner.next:
            if runner.data > runner.next.data:
                runner.data, runner.next.data = runner.next.data, runner.data
            runner = runner.next
        cur = cur.next
    return head


head = Node(1, Node(2, Node(4)))
# head = Node(1)


def start():
    global head
    print(head)

    head = insert_end(head, 3)
    print(head)

    head = bubble_sort(head)
    print(head)
    print(detect_loop(head))

    head = delete_node(head, 2)
    print(head)

    print(search(head, 3))
    print(search(head, 9))
    print(reverse(head))