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

            i += 1
            curr = curr.next

        return -1
        
    def insertHead(self, val: int) -> None:
        new_node = LinkedNode(val)
        new_node.next = self.head.next
        
        self.head.next = new_node

        if new_node.next == None:
            self.tail = new_node


    def insertTail(self, val: int) -> None:
        self.tail.next = LinkedNode(val)
        self.tail = self.tail.next

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
        curr = self.head.next
        values = []

        while curr:
            values.append(curr.val)
            curr = curr.next

        return values