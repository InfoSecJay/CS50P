def main():
    x = int(input("Whats x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
      
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else: 
#         return False
        

#We can refind the above!

# def is_even(n):
#    return True if n % 2 == 0 else False
        

#We can even do better!!!!! Dont ned to include the 

def is_even(n):
   return n % 2 == 0

main()