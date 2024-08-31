# ask user for their name, strip whitespace, and capitalize the title (first/last name)
name = input("Whats your name? ").strip().title()

#Split users name into the first and last
first, last = name.split(" ")

# Say hello to the user
print(f"Hello, {first}")