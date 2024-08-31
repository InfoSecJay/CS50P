#print("Hello World")

# Ask user for their name
name = input("Whats your name? ")

"""
This is a multi-line comment
print to screen

"""

# print("Hello " + name)
# print("What a great name," , name)
# print(f'Your Name is {name}')


"""
print(*objects, sep=" ", end='\n', file=sys.stdout, flush=False)    

- everything between () is a parameter
- the inputs of the parameters are the arguments
- *objects means the function can take any number of arguments
- sep=" " means the seperator, whn you pass multiple arguments, they are seperated by a space
- end='\n' means every line ends with a new line
- file and flush not discussed in lecture
- can use double or single quotes, same thing!
- escape strings with "\"
"""

#print("hello, ", end="???")a

#print("hello, ", name, end="\n")

# add quotations in text?

#print("hello, \"friend\"", name)

#print(f"Hello {name}")

"""
handle when user inputs weird stuff - here we can strip off whitespace
""" 
name = name.strip()
name = name.capitalize() # capitlizes just first letter
name = name.title() # this fixes it so if you give first/last it captilzies both

print(f"Hello {name}")