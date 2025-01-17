# Reverse every word in a string
# swap case of character

s = "Welcome to Python Programming. Learning Python is fun" # Output needed = "OLLEh DLROw"
new_s = ""

word_list = s.split(" ") # ["Hello", "World"]

for word in word_list:
    reversed_word = word[::-1]
    swapped_case = reversed_word.swapcase()
    new_s += swapped_case + " "

new_s = new_s.rstrip()

print(new_s)
