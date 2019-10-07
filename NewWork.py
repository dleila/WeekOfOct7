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

# having a sentence be broken in the middle n joined together by adding them
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
