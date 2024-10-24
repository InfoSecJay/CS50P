class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0 
        
    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n >= 12:
            raise ValueError("Too many cookies in jar")
        self.size += n

    def withdraw(self, n):
        if n <= 0:
            raise ValueError("No more cookies left to take!")        
        self.size -= n
        
    @property
    def capacity(self):
        self._capacity
        
    @capacity.setter    
    def capacity(self, capacity):
        self._capacity
        
    @property
    def size(self):
        self._size

    @size.setter
    def size(self, size):
        self._size
    
    
    


def main():
    jar = Jar()
    print(jar)
    jar.deposit(5)
    print(jar)
    
main()