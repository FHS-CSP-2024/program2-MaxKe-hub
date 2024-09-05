# Information from the user #
#**Learning objectives**
#
#After this section:
#
#* You will know how to write a program which uses input from the user
#* You will know how to use variables to store input and print it out
#* You will be able to combine strings



## Live Demo ##
#
# Input from user
#name = input("What is your name? ")
#print("Hi there, " + name)
#
#name = input("What is your name? \n")
#print("Hi there, " + name)
#print("hi, " + name)
# Talk about Variables
#   * Note python is untyped and loose
#
# Reference a Var
#name = input("What is your name? ")
#print("Hi, ")
#print(name)
#print("!")
#print(name + " is quite a nice name.")
#print("Hi, ")
#print(name)
#print("!")
#print(name + " is quite a nice name!")
#
# Concat w/ +
#name = input("What is your name? ")
#print("Hi " + name + "! Let me make sure: your name is " + name + "?")
#
#print("Hi " + name + "! Let me make sure: your name is " + name + "?")
#x = 7
#print (x + x + x + x)
# Multiple Input
#name = input("What is your name? ")
#email = input("What is your email address? ")
#nickname = input("What is your nickname? ")
#print("Let's make sure we got this right")
#print("Your name: " + name)
#print("Your email address: " + email)
#print("Your nickname: " + nickname)
#
#name = input("TELL ME YOUR NAME!!! ")
#email = input("QUICK TELL ME YOUR EMAIL ")
#nickname = input("What is your nickname? ")
#print("Let's make sure we got this right")
#print("Your name: " + name)
#print("Your email address: " + email)
#print("Your nickname: " + nickname)
# Overriding Input
#name = input("What is your name? ")
#print(name)
#name = input("What is another name? ")
#print(name)
#candy = input("What is your favorite candy? ")
#print(candy)
#candy = input("What is your least favorte candy ")
#print(candy)
## Problem 1 ##
#Please write a script that: 
# - Asks for the user's name and then prints it twice, on two consecutive lines.
print("Problem 1:")
hwname = input("What is your name? \n")
print(hwname)
print(hwname)




## Problem 2 ##
#Please write a script that: 
# - Asks for the user's name
# - Prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, 
# - another between the two names and a third one at the end of the line.
print("Problem 2:")
hwname2 = input("What is your name ")
print("!" + hwname2 + "!" + hwname2 + "!")

## Problem 3 ##
#Please write a script that: 
# - Asks for the user's name and address. 
# - The program should also print out the given information, as follows:
#   - Sample output
#   - First name: Steve
#   - Last name: Sanders
#   - Street address: 91 Station Road
#   - City and postal code: Folsom CA, 95630
print("Problem 3:")

first = input("What is your first name? ")
last = input("What is your last name? ")
adress = input("Where do you live? ")
city = input("What is your city and postal code? ")
print("First name: " + first)
print("Last name: " + last)
print("Street adress: " + adress)
print("City and postal code: " + city)
## Problem 4 ##
#Please write a script that: 
# - Asks for 3 words 
# - Puts the words together with dashes and prints that out
print("Problem 4:")
word1 = input("type a word: ")
word2 = input("type another word: ")
word3 = input("type ANOTHER word: ")
print(word1 + "-" + word2 + "-" + word3)
## Problem 5 ##
#Please write a script that: 
# - Asks for a name and a year
# - Prints out a short story that uses that information
# Sample output:
#Please type in a name: Mary
#Please type in a year: 1572
# ----------------------------------------------
#Mary is a valiant knight, born in the year 1572. 
#One morning Mary woke up to an awful racket: a dragon was approaching the village. 
#Only Mary could save the village's residents.
print("Problem 5:")
prot = input("type in a name: ")
date = input("give me a year: ")
print(prot + " was sitting on a wall in " + date + ".\n" + prot + " then, after repeatedly told to be careful, fell off the wall") 