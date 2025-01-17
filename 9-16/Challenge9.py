# Tokenizing CSV string
#CSV = Comma-Separated Values
#--------
#Option 1
#--------
# string = "name,age,city"
# tokens = []
# current_token = ""
#
# for char in string:
#     if char == ",":
#         tokens.append(current_token)
#         current_token = ""
#     else:
#         current_token += char
# tokens.append(current_token)
#
# print(tokens)
# 1st: char="n"; current_token = "n";    tokens = []
# 2nd: char="a"; current_token = "na";   tokens = []
# 3rd: char="m"; current_token = "nam";  tokens = []
# 4th: char="e"; current_token = "name"; tokens = []
# 5th: char=","; current_token = "";     tokens = ["name"]
# 6th: char="a"; current_token = "a";    tokens = ["name"]
# 7th: char="g"; current_token = "ag";   tokens = ["name"]
# 8th: char="e"; current_token = "age";  tokens = ["name"]
# 9th: char=","; current_token = "";     tokens = ["name","age"]
#10th: char="c"; current_token = "c";    tokens = ["name","age"]
#11th: char="i"; current_token = "ci";   tokens = ["name","age"]
#12th: char="t"; current_token = "cit";  tokens = ["name","age"]
#13th: char="y"; current_token = "city"; tokens = ["name","age"]




#--------
#Option 2
#--------

# string = "name,age,city"
# tokens = string.split(",")
# print(tokens)









#--------
#Option 3
#--------

import csv

string = "name,age,city"
tokens = list(csv.reader([string]))[0]
print(tokens)

# string = "name,age,city"
# [string] = ["name,age,city"];
# list(csv.reader(["name,age,city"]))[0]
# tokens = list([["name","age","city"]])[0]
# tokens = ["name","age","city"]
