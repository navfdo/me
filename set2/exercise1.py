"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# This defines the set of some_words
some_words = ["what", "does", "this", "line", "do", "?"]
# I think it will print all the words within the list "some_words"
for word in some_words:
    print(word)  # It printed all the words in the list
# It will print every item in the list
for x in some_words:
    print(x)  # Printed every item in the list

print(some_words)

if len(some_words) > 3:
    print("some_words contains more than 3 words")


def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())


usefulFunction()
