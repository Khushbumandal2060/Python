#TASK2:  Wap to identify whether the entered character is vowel or not ?u
# Input from the user
char = input("Enter a single character: ")

# Check if the character is a vowel
if char.lower() in "aeiou" and len(char) == 1:
    print(f"The character '{char}' is a vowel.")
else:
    print(f"The character '{char}' is not a vowel.")
