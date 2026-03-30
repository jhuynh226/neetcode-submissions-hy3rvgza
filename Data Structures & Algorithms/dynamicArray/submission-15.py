class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [0] * capacity


    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length >= self.capacity:
            self.resize()


        self.array[self.length] = n
        self.length += 1


    def popback(self) -> int:
        element = self.array[self.length - 1]
        self.length -= 1

        return element

    def resize(self) -> None:

        newArray = [0] * (self.capacity * 2)

        for i in range(self.length):
            newArray[i] = self.array[i]

        self.array = newArray.copy()
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity