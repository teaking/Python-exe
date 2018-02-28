inp = input("Enter Char in Uppercase: ")
if inp >= 'A' and inp <= 'Z':
    #ord is used to get alphabet sequence num and chr to 
    #convert int to char
    print('value', chr(ord(inp) - ord('A') + ord('a')))
        
