from sys import argv

script, user_name, user_id = argv
prompt = '> '

print "Hi %s , your user name is %s. I'm the %s script." % (user_name, user_id, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have %s" % user_name
computer = raw_input(prompt)

print """
Alright, So you said %r about liking me.
You live in %r. Not sure where that is.
and you have a %r computer. Nice.
""" % (likes, lives, computer)


