# while True:
#     n = input("Whats n?")
#     if n < 0:
#         continue
#     else:
#         break

"""while True:
    n = int(input("Whats n?"))
    if n > 0:
        break

for _ in range(n):
    print("meow")"""
    
    
def main():
    number =  get_number()
    meow(number)
    
    
def get_number():
    while True:
        n = int(input("Whats n?"))
        if n > 0:
            return n
        
def meow(n):
    for _ in range(n):
        print("meow")
        
main()