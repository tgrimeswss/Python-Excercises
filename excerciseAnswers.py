# Exercise 1.
# The function takes in the a_list list. Utilizing a for loop, it will iterate
# through the list and eachtime will create a conditional statement checking to
# see if the number is == 1. If it is, the counter variable is iterated by 1.
# If it isn't, it will move on and iterate the next value in the list. It will
# then print the counter when the loop is fully executed

# a_list = [1,3,55,1,9,4,56,2,1,8]
# def countOnes(numbers):
#     counter = 0
#     for x in numbers:
#         if x == 1:
#             counter = counter + 1
#     print (counter)
#
# countOnes(a_list)

#-------------------------------------------------------------------------------

# Exercise 2.
# This function takes in a string argument. It starts off by establishing two
# counter variables. Then it iterates through each character of the string Then
# checks to see if the character is a letter or number utilizing the isalpha and
# isdigit function. The counter(s) are iterated everytime a letter or number is
# triggered. Then it prints a user friendly string stating how many letters
# and how many numbers were in the string

# def stringOrNum(string):
#     counter = [0,0]
#     for x in string:
#         if x.isalpha() == True:
#             counter[0] = counter[0]+1
#         elif x.isdigit() == True:
#             counter[1] = counter[1] + 1
#     print ('# of letters = ' + str(counter[0]) + '\n# of digits = ' + str(counter[1]))
#
# stringOrNum('Test123')

#-------------------------------------------------------------------------------

# Exercise 3 (Reverse order words)
# My function takes in a string that will create a new variable that iterates
# a string in reverse. The new variable (string) is then printed out

# def bassAckwards(string):
#     string = string[::-1]
#     print (string)
#
# bassAckwards('python')
# bassAckwards('star')
# bassAckwards('green')
# bassAckwards('yellow')

#-------------------------------------------------------------------------------

# Exercise 4 (Temp converter)
# My function takes in a number parameter, which specifies the current Celcius
# temperature. It equates the celcius temp to farenheit by setting a farenheit
# variable. After the math is complete and the 'f' variable is established, it
# will run a few conditions to test and see where that farenheit temperature lies
# (Is it too hot or too cold)

# def tempConverter(c):
#     f = c * 9/5 + 32
#     if f > 90:
#         print "a heat warning"
#     elif f < 30:
#         print "a cold warning"
#     print(f)
#
# tempConverter(0)
#-------------------------------------------------------------------------------

# Exercise 5 (Vowel Vs. Consonant)
# If the letter is considered a vowel or 'y', it will trigger a print method telling
# the user that it is in fact a vowel. If it does not pass the criteria, the program
# will tell the user that the letter is a consonant.

# def consonant(letter):
#     if letter == 'a':
#         print('vowel')
#     elif letter == 'e':
#         print('vowel')
#     elif letter == 'i':
#         print('vowel')
#     elif letter == 'o':
#         print('vowel')
#     elif letter == 'u':
#         print('vowel')
#     elif letter == 'y':
#         print('sometimes y is a consonant')
#     else:
#         print 'consonant'

#-------------------------------------------------------------------------------

# Excercise 6. (pyramidPattern)
# My function takes in a number, which will change the pyramid row size depending
# on what the user puts in. It starts off with a for loop printing a space, a '*',
# then iterating to print an additional star but REMAINING with one space. When
# the loop is completely executed, it goes into a second loop (not nested), which
# then completes the same loop as the above however it does the '*' counting in reverseself.
# The space iteration does not change.

# def pyramidPattern(rows):
#     for i in range(rows):
#         print(''*(rows-i-1)+'* '*(i+1))
#     for x in range(rows-1,0,-1):
#         print (''*(rows-x)+"* "*(x))
#
# pyramidPattern(5)
#-------------------------------------------------------------------------------


# Exercise 7 (FizzBuzz)
# The AND condition is operated first due to the fact it is most
# specific in nature and will execute only if the criteria is met. Then the remaining
# three operators check to see if the number is divisible by 3,5 or return just the number
# if it is not divisible by either

# for i in range(1,101):
#     if i % 3==0 and i % 5==0:
#         print str(i) + ' FizzBuzz'
#     if i % 3 == 0:
#         print str(i) + ' Fizz'
#     elif i % 5 == 0:
#         print str(i) + ' Buzz'
#     else:
#         print i

#-------------------------------------------------------------------------------

# Exercise 8 (Multiplication Table)

# I created a function that takes in a number. The number refers to how large the
# user wants the table to be. The first line prints a tab. Then it initiates a for
# loop that prints a same line list starting at zero and ending at the number specified
# by the user. Then nested loop multiplies a static iteration by a dynamic. Then
# after it executes the inner loop, it will print a new line and complete the new
# multiplication line.

# def multiplicationTables(list):
#     print(end="\t")
#     for x in range(list):
#         print(x,end="\t")
#     print('\n')
#     for i in range(list):
#         for a in range(list):
#             print (i * a, end = "\t")
#         print('\n')
#
# multiplicationTables(10)
#-------------------------------------------------------------------------------


# Example 9 (Palindrome checker)
# The function takes in a string parameter. If the text in reverse(line 160) is
# equal to the actual text, it will print 'True'. If it is not, it will print false

# def palindrome(text):
#     if text == text[::-1]:
#         print (True)
#     else:
#         print (False)
#
# palindrome('anna') #Test will pass
# palindrome('Thomas') #Test will not pass


#-------------------------------------------------------------------------------
# Example 10 (Ceasar cypher)
# Currently working on a decoder function as well as a 'shift' parameter.
# The key is a dictionary that assigns a string value to a string key. Then
# a for loop will create a space everytime there is NO key value pair is found in
# in the dictionary labeled 'key'. If the key is found, the nested loop will append the
# found value to the starting empty decrypted string. Then it will print the
# decrypted string.

# As mentioned, I am still currently working on inputting the shift parameter
# as well as a decypher function.

# def cipher(text):
#     text = text.lower()
#     decrypted = ' '
#     key = {
#         'a':'n', 'b':'o', 'c':'p', 'd':'q',
#         'e':'r', 'f':'s', 'g':'t', 'h':'u',
#         'i':'v', 'j':'w', 'k':'x', 'l':'y',
#         'm':'z', 'n':'a', 'o':'b', 'p':'c',
#         'q':'d', 'r':'e', 's':'f', 't':'g',
#         'u':'h', 'v':'i', 'w':'j', 'x':'k',
#         'y':'l', 'z':'m',
#     }
#     for i in text:
#         if i not in key.values():
#             decrypted += i
#         else:
#             for value in key:
#                 if value == i:
#                     decrypted += key[i]
#
#     print (decrypted)
#
# cipher('This is a test sentence')
