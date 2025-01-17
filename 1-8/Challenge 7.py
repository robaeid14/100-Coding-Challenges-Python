#Challange 7
#Remove character at a specific INDEX
#--------
#option 1
#--------
# s = "" #W o r l d
# n = 5  #0 1 2 3 4
#
# if (len(s)==0) or n >= len(s):
#     print(s)
# else:
#     new_s = ""
#     for i in range(len(s)):
#         if i != n:
#             new_s += s[i]
#
#     print(new_s)

#World - n=3
#1st: i=0, new_s = "W"
#2nd: i=1, new_s = "Wo"
#3rd: i=2, new_s = "Wor"
#4th: i=3
#5th: i=4, new_s = "Word"

#--------
#option 2
#--------
# s = "" #W o r l d
# n = 5  #0 1 2 3 4
#
# if (not s) or n >= len(s):
#     print(s)
# else:
#     new_s = ""
#     for i in range(len(s)):
#         if i != n:
#             new_s += s[i]
#
#     print(new_s)

