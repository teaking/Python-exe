"""return the largest word in the string"""
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def main():
    print(longestWrd(removePunctuation("we!!!!! ares dogs.")))

'''removes the chracters found in "punctuations" '''
def removePunctuation(words):
    no_punct = ""
    for i in words:
        if i not in punctuations:
            no_punct += i
    return no_punct

'''checks the provided strings and outputs the longest word found first'''            
def longestWrd(sen):
    words = sen.split(" ")
    word = words[0]
    #check the longest word
    for i in words:
        if len(word) < len(i):
            word = i
    return word 

main()
