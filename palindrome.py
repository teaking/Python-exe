def main():
    newStrInput = input("Input string to reverse - ")
    print (palindrome(newStrInput))

'''reverse user input'''
def palindrome(user_inp):
    return user_inp[::-1]




main()
