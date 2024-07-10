

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        if type(capacity) != int:
            raise ValueError("Capacity must be an intiger ")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        
        return self.size * "🍪"

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies")
        if self.size + n <= self.capacity:
            self._size += n
        else:
            raise ValueError("Deposit exceeds jar capacity")

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies")
        if self.size - n >= 0:
            self._size -= n
        else:
            raise ValueError("Not enough cookies to withdraw")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar()
    print(jar)
    jar.deposit(9)
    print(jar)
    jar.withdraw(3)
    print(jar)
    
    
    # jar.deposit(10)
      # This will raise a ValueError


if __name__ == "__main__":
    main()
