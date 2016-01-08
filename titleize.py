function_words = ['or', 'and', 'but', 'a', 'an', 'the', 'of', 'for', 'on', 'to', 'while', 'because', 'before', 'how', 'when', 'where', 'as', 'if', 'after', 'though', 'in', ]

inp = raw_input("Enter a text: ")
words = inp.split()

for word in words:
    if word.lower() in function_words:
        print word.lower(),
    else:
        print word[0].upper() + word[1:].lower(), 

