# Write a function is_even that will return true if the passed-in number is even.
def is_even(num):
    return num % 2 == 0
# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
print(is_even(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def is_even2(num):
    return 'Even' if num % 2 == 0 else 'Odd'

print(is_even2(num))
