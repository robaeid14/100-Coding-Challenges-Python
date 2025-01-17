# --------
#OPTION 1
# --------
# s = ""
# new_s = ""
#
# for i in range(len(s)):
#     if i%2 != 0:
#         new_s += s[i]
#
# print(new_s)











# --------
#OPTION 2
# --------
s = "Python" # y  h  n
new_s = ""   # 1  3  5

for i in range(1,len(s),2):
        new_s += s[i]

print(new_s)