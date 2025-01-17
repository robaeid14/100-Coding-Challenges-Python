#CHALLENGE 10
#CHECK IF A String IS PANGRAM OR NOT
#--------------------------------------------------------
# A pangram is a string/sentence that
# contains all the letter in the alphabet at least onece
#--------------------------------------------------------




#---------
# Option 1
#---------
# import string
#
# s = "The quick brown fox jumps over the lazy dog"
#
# set_s = set(s.lower())
#
# set_s.remove(" ")
#
# print(set_s == set(string.ascii_lowercase))












#---------
# Option 2
#---------
# import string
#
# s = "The quick brown fox jumps over the lazy dog"
#
# is_pangram = True
#
# for char in string.ascii_lowercase:
#     if char not in s.lower():
#         is_pangram = False
# #ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
# print(is_pangram)











# ---------
# Option 3
# ---------
import string

s = "The quick"

is_pangram = True

for char in string.ascii_lowercase:
    if char not in s.lower():
        is_pangram = False
        break #exit the loop immediately
        #if false no need to compare further

print(is_pangram)