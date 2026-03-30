class LinkedNode:
    def __init__(self, val=-1):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.dummy_head = LinkedNode()
        self.dummy_tail = LinkedNode()

        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def isEmpty(self) -> bool:
        return self.dummy_head.next == self.dummy_tail

    def append(self, value: int) -> None:
        node = LinkedNode(value)
        node.next = self.dummy_tail
        node.prev = self.dummy_tail.prev
        self.dummy_tail.prev.next = node
        self.dummy_tail.prev = node

    def appendleft(self, value: int) -> None:
        node = LinkedNode(value)
        node.next = self.dummy_head.next
        node.prev = self.dummy_head
        self.dummy_head.next.prev = node
        self.dummy_head.next = node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        value = self.dummy_tail.prev.val
        self.dummy_tail.prev.prev.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_tail.prev.prev

        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        value = self.dummy_head.next.val
        self.dummy_head.next.next.prev = self.dummy_head
        self.dummy_head.next = self.dummy_head.next.next 

        return value
