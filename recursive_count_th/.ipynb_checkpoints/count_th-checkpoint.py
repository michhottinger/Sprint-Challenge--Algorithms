'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # the word needs to be two letters or more in length
    # check the first two letters then increment and go forward
    #if the first letter is not th, then check one by one
    
    if len(word) < 2:
        return 0
    elif word[0:2] == "th":
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])
    
