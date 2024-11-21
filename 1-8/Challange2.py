#CHALLANGE 2
#FIND THE CHARACTER AT A SPECIFIC INDEX

# --------------------
# Option 1
# --------------------

# myString = "Python" # P y t h o n
# i = 7               # 0 1 2 3 4 5
#
# if len(myString) == 0:
#     print("String is empty.")
# elif i< len(myString):
#     print(myString[i])
# else:
#     print("Out of range.")






# --------------------
# Option 2
# --------------------

myString = ""
i = 0

if not myString:  #truthy falsy
    print("String is empty.")
elif i < len(myString):
    print(myString[i])
else:
    print("Out of range.")