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
        if self.length == self.capacity:
            self.resize()

        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        popped_value = self.array[self.length - 1]
        self.array[self.length - 1] = 0
        self.length -= 1

        return popped_value

    def resize(self) -> None:
        self.capacity *= 2
        self.new_array = [0] * self.capacity

        for i in range(len(self.array)):
            self.new_array[i] = self.array[i]

        self.array = self.new_array

    def getSize(self) -> int:
        return self.length
        
    def getCapacity(self) -> int:
        return self.capacity
