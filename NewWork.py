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
# Because %r can be put there all by itself while %s needs a sentence to be places in
