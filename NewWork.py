# putting a number in a sentence
x = "There are %d types of people." % 10
binary = "binary"
doNot = "don't"
# putting binary and don't into a sentence
y = "Those who know %s and those who %s." % (binary, doNot)

# having the computer write the sentence
print(x)
print(y)

# repeating what I said
print("I said: %r" % x)
print("I also said: '%s'." % y)

# having the sentence ask a question and the answer being false
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)

# having a sentence be broken in the middle and joined together by adding them
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

# More stuff 10-8

# Saying Mary had a little lamb
print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
# Had the "." multiplied by 10 making it become ".........."
print("." * 10)

# Making definitions for end1-12
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Stringing the word together by adding it
print(end1 + end2 + end3 + end4 + end5 + end6 + end7 + end8 + end9 + end10 + end11 + end12)

# More Formatting
formatter = "%r %r %r %r"
# Numbers in actual number form
print(formatter % (1, 2, 3, 4))
# Numbers in letter form
print(formatter % ("one", "two", "three", "four"))
# Using formatter to put in what I put in the second parentheses without commas
print(formatter % (True, False, False, True))
# Formatter in %r as I said up above so when I format formatter I get a lot of %rs
print(formatter % (formatter, formatter, formatter, formatter))

# Why did I use %r instead of %s?
# Because %r can be put there all by itself while %s needs a sentence to be placed in

# Time for some strange stuff in the world of printing...
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nJun\nJul\nAug"
print("Here are the days: ", days)
print("Here are the months: ", months)

# You don't have to put print in front of every line, you just put (""" and """) at the beginning and end of every line
print("""
There is something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

# What if I didn't like Jan being listed on the line with the rest of the
# text and many from the other months? How could I fix that?
# You could put \n so it puts each word on a different line

# More escaping
tabbyCat = "\tI'm tabbed in."
# put \n before the word you want to be moved down a line
persianCat = "I'm split\non a line."
# talking without having to say print
taskCat = """
I'll make a list: 
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabbyCat)
print(persianCat)
print(taskCat)

# Escape Seq
# \\
# \'
# \"
# \a
# \b
# \f
# \n
# \N{name}
# \r
# \t
# \uxxxx
# \Uxxxxxxxx
# \v
# \ooo
# \xhh

# What's the following code do:
#  while True
#       for i in ["/","-","|","\\","|"]:
#           print("%s\r" % i, end='')

# Can you replace """ with '''
# Yes if you do a little definition beforehand and put something like """ = '''

# Asking Questions

age = input("How old are you? ")
height = input("How tall are you? ")

print("So, you really %r old are %r tall? Wow...." % (age, height))