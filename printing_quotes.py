#Printing Quotes

quote = input("what is the quote?")
author = input("who said it?")

#string interpolation (f-string)
print(f'{author} says,\"{quote}\".')

#string concatenation
print( author + " says, \"" + quote + ".\"")
'''
this is my first time experimenting with string interpolation using f-string.

lesson learned: 
    
    a SyntaxError will appear if you place backslashes within the curly braces of the expression.
    also, I experimented with using docstrings and comments. 

'''
