class LinkedNode:
    def __init__(self, val):
        self.val = val 
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.dummy = LinkedNode(-1)
        self.head = self.dummy
        self.tail = self.dummy
    
    def get(self, index: int) -> int:
        cur, i = self.head.next, 0

        while cur and i <= index:
            if i == index:
                return cur.val

            cur = cur.next
            i += 1

        return -1        

    def insertHead(self, val: int) -> None:
        node = LinkedNode(val)
        node.next = self.dummy.next
        self.dummy.next = node

        if node.next == None:
            self.tail = node

    def insertTail(self, val: int) -> None:
        node = LinkedNode(val)
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        cur, prev = self.head.next, self.dummy 
        i = 0
        
        while cur and i <= index:
            if i == index:
                if cur == self.tail:
                    self.tail = prev

                prev.next = prev.next.next
                return True
            
            prev = cur
            cur = cur.next
            i += 1

        return False

    def getValues(self) -> List[int]:
        cur, values = self.dummy.next, []

        while cur:
            values.append(cur.val)
            cur = cur.next

        return values