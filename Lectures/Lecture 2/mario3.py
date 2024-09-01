"""
    Prints a Square
"""

def main():
    print_square(4)
    
    
def print_square(size):
    
    # for each row in square
    for i in range(size):
        
        # for each brick in row
        for j in range(size):
            
            # print brick
            print("#", end="")  
            
        print() #  print with no arguments is \n
        
main()



