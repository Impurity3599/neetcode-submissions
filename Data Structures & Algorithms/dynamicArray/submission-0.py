class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dynamicArray = [0] * self.capacity
        self.size = 0

    def get(self, i: int) -> int:
        if self.size == 0 or i < 0 or i >= self.capacity:
            ThrowNewException("OOB")
        return self.dynamicArray[i]

    def set(self, i: int, n: int) -> None:
            self.dynamicArray[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.dynamicArray[self.size] = n
        self.size+=1

    def popback(self) -> int:
        if self.size > 0:
            self.size-=1

        return self.dynamicArray[self.size]

    def resize(self) -> None:
        self.capacity *=2
        newDynamicArray = [0] * self.capacity

        for idx in range(self.size):
            newDynamicArray[idx] = self.dynamicArray[idx]

        self.dynamicArray = newDynamicArray

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity