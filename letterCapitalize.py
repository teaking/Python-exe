'''capitalize the first letter of each word. Words will be seperated by 
one space'''


def main():
    usr_inp = input("USER INPUT: ")

    print(letterCapitalize(usr_inp))

def letterCapitalize(usr_inp):
    capitalizeLetters = ""
    usr_inp = usr_inp.split(" ")
    for words in usr_inp:
        capitalizeLetters += words.capitalize() + " "

    return capitalizeLetters


main()
