class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = LinkedNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next

        while curr:
            if i == index:
                return curr.val

            curr = curr.next
            i += 1

        return -1
        

    def insertHead(self, val: int) -> None:
        node = LinkedNode(val)
        node.next = self.head.next

        self.head.next = node

        if not node.next:
            self.tail = node
        

    def insertTail(self, val: int) -> None:
        node = LinkedNode(val)
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head

        while curr and i < index:
            curr = curr.next
            i += 1

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr

            curr.next = curr.next.next
            return True

        return False
        

    def getValues(self) -> List[int]:
        values = []
        curr = self.head.next

        while curr:
            values.append(curr.val)
            curr = curr.next

        return values

