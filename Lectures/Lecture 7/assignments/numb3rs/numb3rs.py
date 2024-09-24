import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Simple, Not accurate: https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch07s16.html    
    # matches = re.search(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', ip)
    
    #Accurate: https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch07s16.html
    # matches = re.search(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip)               
    
    # Accurate regex for an IP address (common standard)
    if matches :=  re.search(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()