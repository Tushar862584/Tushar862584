class Jar:
    def __init__(self, capacity=12) -> None:
        self.capacity = capacity
        self.size = 0

    def __str__(self) -> str:
        return f"{'🍪'*self.size}"

    def deposit(self, n: int) -> None:
        self.size += n

    def withdraw(self, n: int) -> None:
        self.size -= n

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self,capacity: int) -> None:
        if capacity < 0:
            raise ValueError("Invalid capacity of the jar")
        self._capacity = capacity

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self,size: int) -> None:
        if size < 0:
            raise ValueError("Too few cookies")
        if size > self.capacity:
            raise ValueError("Too many cookies")
        self._size = size


jar = Jar()
jar.deposit(2)
jar.withdraw(1)
print(jar)
