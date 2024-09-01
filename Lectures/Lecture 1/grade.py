score = int(input("Score: "))

# if score >= 90 and score <= 100:
#     print("Grade A")
# elif score >= 80 and score < 90:
#     print("Grade B")
# elif score >= 70 and score < 80:
#     print("Grade B")
# elif score >= 60 and score < 70:
#     print("Grade B")
# else:
#     print("Grade F")


# Chaining Comparison Operaters : instead of asking two questions like above, just shorted it (minor improvement to do less steps)


if 90 <= score <= 100:
    print("Grade A:")
elif 80 <= score <= 90:
     print("Grade B")
elif 70 <= score <= 80:
     print("Grade C")
elif 60 <= score <= 70:
     print("Grade D")
if:
     print("Grade F")
     
    
"""THIS IS BAD - it will print out every Grade!
if 90 <= score <= 100:
    print("Grade A:")
if 80 <= score <= 90:
     print("Grade B")
if 70 <= score <= 80:
     print("Grade C")
if 60 <= score <= 70:
     print("Grade D")
if:
     print("Grade F")"""
     
     
     