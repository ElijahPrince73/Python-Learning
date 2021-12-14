myString = "Hello world!"

print(myString[0])
# returns H

# Using negative numbers allows for us to start at the end of the string
print(myString[-3])
# returns l

newString = "abcdefghijklmnop"

# String slicing
# left of the colon is the start of the string and the right of the colon is the end or the stoping point

print(newString[2:])
# returns cdefg

print(newString[:3])
# returns abc

print(newString[3: 6])
# returns def

# Allows us to skip a character
print(newString[::2])
# returns aceg

# We can still decide how we want to slice the string by providing additional arguments

print(newString[2:7:2])
# returns ceg