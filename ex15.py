from sys import argv 
script, filename = argv

# open the file provided by the user
txt = open(filename)

print "file name %r:" %filename
# commanding the file to use read command with 
# no parameters
print txt.read()
# close file 
# important to always close file when opened
txt.close()

print "type the file name again:" 
# prompting and reading user input
filename_again = raw_input("> ")

txt_again = open(filename_again)
# commanding the file to use read command with 
# no parameters
print txt_again.read()
# close file 
# important to always close file when opened
txt_again.close()


