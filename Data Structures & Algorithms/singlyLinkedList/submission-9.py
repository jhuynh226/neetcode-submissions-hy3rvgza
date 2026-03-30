class LinkedNode:
    def  __init__(self, val):
        self.val = val 
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = LinkedNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0

        while cur and i <= index:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        
        return -1
        
    def insertHead(self, val: int) -> None:
        new_node = LinkedNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        if new_node.next == None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = LinkedNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        cur = self.head.next
        prev = self.head
        i = 0

        while cur and i <= index:
            if i == index:
                if cur == self.tail:
                    self.tail = prev
                    self.tail.next = None
                    return True
                else:
                    prev.next = prev.next.next
                    return True 

            cur = cur.next
            prev = prev.next
            i += 1

        return False

    def getValues(self) -> List[int]:
        values_list = []

        cur = self.head.next

        while cur:
            values_list.append(cur.val)
            cur = cur.next
        
        return values_list