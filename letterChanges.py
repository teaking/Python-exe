def main():
    user_inp = input("Enter word")
    print(letterChange(user_inp))

def letterChange(usr_inp):
    word = ""
    for characters in usr_inp:
        if returnAsciiVal (characters) >= returnAsciiVal('a') and returnAsciiVal(characters) <= returnAsciiVal('z'):
            if characters != 'z':
                word += chr(returnAsciiVal(characters) + 1)      
            else:
                 #hard coding 97 == a
                word += 'a'
        else:
            word += characters
    return word

def returnAsciiVal(characters):
    return ord(characters) 


main()
