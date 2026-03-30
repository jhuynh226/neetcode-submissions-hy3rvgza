class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [0] * capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        popped_element =  self.array[self.length - 1]
        self.length -= 1

        return popped_element

    def resize(self) -> None:
        newArray = [0] * (self.capacity * 2)

        for i in range(len(self.array)):
            newArray[i] = self.array[i]

        self.array = newArray
        self.capacity *= 2


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
