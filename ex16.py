from sys import argv

script, filename = argv 

print "Erasing the file %r:" %filename

print "If do not want that, hit CTRL-C (^C)."
print "If you do want, hit RETURN."

raw_input("?")

print ("Opening file....")
# opening file with write permission
target = open(filename,'w')

print "truncating the file. Goodbye!"
# empties the file 
target.truncate()

print "three lines."
# reading user input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Writing three line got from user"
# writing on file
target.write("%s\n%s\n%s\n" % (line1,line2,line3)) 

print "We are done. We close it."
# close the file
target.close()

print "Enter the newly created file name"
target_file = raw_input("> ")
new_txt_file = open(target_file)
print new_txt_file.read()
new_txt_file.close()
