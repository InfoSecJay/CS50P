class Jar:
           
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0 # initialize the size which is 0

    def __str__(self):
        return self.size * '🍪'
    
    def deposit(self, n):
        # if self.capacity > 12 or self.size + n > self.capacity:  # wrong....
        if n > self.capacity or self.size + n > self.capacity:
            raise ValueError("Exceed cookie jars capacity")
        self.size += n
  
    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Arent enough cookies left")
        self.size -= n
        
    @property # Getter
    def capacity(self):
       return self._capacity

    @capacity.setter #Setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Invalid capacity")
        self._capacity = capacity
   
    @property # Getter
    def size(self):
        return self._size

    @size.setter  #Setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Invalid size")
        self._size = size


# def main():
#     jar = Jar()
#     jar.deposit(2)
#     print(jar)
#     jar.deposit(8)
#     print(jar)
#     jar.withdraw(4)
#     print(jar)
    
# main()