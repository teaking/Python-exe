# Python script to cpy from one file to another
from sys import argv
# library to check if the file exists
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

in_file = open(from_file, 'r').read()

print """The input file is %d bytes long
Does the output file exists? %r """ % (len(in_file), exists(to_file))

# print "Does the output file exists? %r" % exists(to_file)
# print "Read, hit RETURN to continue, CTRL-C to abort."
# raw_input()

out_file = open(to_file, 'w').write(in_file)

print "Alright, all done."
