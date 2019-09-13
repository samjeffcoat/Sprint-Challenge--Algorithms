'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

##psudocode
## We are going to be recieving a string
## for our base case, we need to exit out our functions because it must contain 2 letters to work, in our case th
#Evaluate the first two letters of the sting
# if th is included in our first two letters:
#   Call the function again (recursion), on the rest of the string minus the first letter, +1 to increment as you go 
# Call the function again (recursion), on it minus our first letter 

def count_th(word):

        key= "th"

        if len(word) <= 1:
            return 0

        if key in word[0:2]:
            return 1 + count_th(word[1:])
        else:
            return count_th(word[1:])