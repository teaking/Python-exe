import pprint
info = '''
SCENE I. Yorkshire. Gaultree Forest.
Enter the ARCHBISHOP OF YORK, MOWBRAY, LORD HASTINGS, and others
ARCHBISHOP OF YORK
What is this forest call'd?
HASTINGS
'Tis Gaultree Forest, an't shall please your grace.
ARCHBISHOP OF YORK
Here stand, my lords; and send discoverers forth
To know the numbers of our enemies.
HASTINGS
We have sent forth already.
ARCHBISHOP OF YORK
'Tis well done.
My friends and brethren in these great affairs,
I must acquaint you that I have received
New-dated letters from Northumberland;
Their cold intent, tenor and substance, thus:
Here doth he wish his person, with such powers
As might hold sortance with his quality,
The which he could not levy; whereupon
He is retired, to ripe his growing fortunes,
To Scotland: and concludes in hearty prayers
That your attempts may overlive the hazard
And fearful melting of their opposite.
MOWBRAY
Thus do the hopes we have in him touch ground
And dash themselves to pieces.
Enter a Messenger
HASTINGS
Now, what news?
Messenger
West of this forest, scarcely off a mile,
In goodly form comes on the enemy;
And, by the ground they hide, I judge their number
Upon or near the rate of thirty thousand.
MOWBRAY
The just proportion that we gave them out
Let us sway on and face them in the field.
ARCHBISHOP OF YORK
What well-appointed leader fronts us here?
Enter WESTMORELAND
MOWBRAY
I think it is my Lord of Westmoreland.
WESTMORELAND
Health and fair greeting from our general,
The prince, Lord John and Duke of Lancaster.
ARCHBISHOP OF YORK
Say on, my Lord of Westmoreland, in peace:
What doth concern your coming?
WESTMORELAND
Then, my lord,
Unto your grace do I in chief address
The substance of my speech. If that rebellion
Came like itself, in base and abject routs,
Led on by bloody youth, guarded with rags,
And countenanced by boys and beggary,
I say, if damn'd commotion so appear'd,
In his true, native and most proper shape,
You, reverend father, and these noble lords
Had not been here, to dress the ugly form
Of base and bloody insurrection
With your fair honours. You, lord archbishop,
Whose see is by a civil peace maintained,
Whose beard the silver hand of peace hath touch'd,
Whose learning and good letters peace hath tutor'd,
Whose white investments figure innocence,
The dove and very blessed spirit of peace,
Wherefore do you so ill translate ourself
Out of the speech of peace that bears such grace,
Into the harsh and boisterous tongue of war;
Turning your books to graves, your ink to blood,
Your pens to lances and your tongue divine
To a trumpet and a point of war?

'''
count = {}
for character in info.upper():
	# return values for the given key if not availabe
	# then return default value none
	count[character] = count.get(character,0) + 1

value = pprint.pformat(count)
print(value)