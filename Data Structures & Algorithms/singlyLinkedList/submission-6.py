class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = LinkedNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0

        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next

        return -1

    def insertHead(self, val: int) -> None:
       node = LinkedNode(val)
       node.next = self.head.next
       self.head.next = node

       if not node.next:
        self.tail = node

    def insertTail(self, val: int) -> None:
        self.tail.next = LinkedNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        cur = self.head

        while i < index and cur:
            cur = cur.next
            i += 1

        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False



    def getValues(self) -> List[int]:
        cur = self.head.next
        values = []

        while cur:
            values.append(cur.val)
            cur = cur.next

        return values


