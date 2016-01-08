function_words = [
'or', 'and', 'but', 'a', 'an', 'the', 'of', 'for', 'on', 'to', 'while',
'because', 'before', 'how', 'when', 'where', 'as', 'if', 'after',
'though', 'although', 'in', 'not', 'than', 'until', 'till', 'that',
]

inp = raw_input("Enter a text: ")
words = inp.split()

print words[0].capitalize(),
for Word in words[1:]:
    word = Word.lower()
    if word in function_words:
        print word,
    else:
        print word.capitalize(),
