#CHALLANGE 4
#PRINT FIRST AND LAST 3 CHARACTER OF A STRING

# --------
#OPTION 1
# --------

# s = "Hello"
# if len(s) < 6:
#     print("String contains less than 6 characters.")
# else:
#     new_s = s[:3] + s[len(s)-3:]
#     print(new_s)

# --------
# OPTION 2
# --------

s = "Beautiful"
total_char = 1

if len(s) < total_char*2:
    print("String contains less than "+str(total_char*2)+" characters.")
else:
    new_s = s[:total_char] + s[len(s) - total_char:]
    print(new_s)
