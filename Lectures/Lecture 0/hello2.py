
# write code logically by defining a main part of the code at the top of the file, define it "main" as a convention that this is main part of the program

def main():
    name = input("Whats your name? ") 
    hello(name)


# define the hello function later in the code

def hello(to="world"):
    print("Hello,", to)
   

# here you can call the main function which will call main, where main() calls hello()

main()
