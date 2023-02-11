""" 
The Python function that accepts a string. This function should count the number of Xs and the number of Os in the string. 
It should then return a boolean value of either True or False.

If the count of Xs and Os are equal, then the function should return True. If the count isn’t the same, it should return False. 
If there are no Xs or Os in the string, it should also return True 
because 0 equals 0. The string can contain any type and number of characters.
"""
word = "xooo"
def check_number_of_x_and_o(a):
    no_of_x = a.count('x')
    no_of_o = a.count('o')
    
    if no_of_x == no_of_o:
        print(True)
    elif no_of_o != no_of_x:
        print(False)
    else:
        print(True)

check_number_of_x_and_o(word)
