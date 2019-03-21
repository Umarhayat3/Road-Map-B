moby_txt = open("moby_01.txt", mode='r').read()
moby_paragraphs = moby_txt.split('\n\n')
moby=moby_paragraphs[1].lower()
print(moby)
for punctuation in [',', '.', '--']:
    moby = moby.replace(punctuation, '')

moby_words = moby.replace('\n', ' ').split(sep=' ')
print(moby_words)
