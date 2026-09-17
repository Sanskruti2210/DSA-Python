'''
Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). 
A word is defined as a sequence of non-space characters. The words in s are separated by at least one space.
Return a string with the words in reverse order, concatenated by a single space.
'''

s = "welcome to the jungle"
words = ""

# init empty count
word = ""

for ch in s:

    # If the char is not white space add it into word
    if ch != ' ':
        word += ch
        
    # If it is space add word before the words
    elif word :
        words = word + ' ' + words
        word = ""
  
# If there is any last word remaining add it      
if word :
    words = word + ' ' + words
    

print(words)