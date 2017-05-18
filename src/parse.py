import pymorphy2
from sys import argv, stderr, exit

if len(argv) != 2:
	stderr.write('Usage: %s your_word' % argv[0])
	exit()

word = argv[1]

morph = pymorphy2.MorphAnalyzer()

res = morph.parse(word)

variants = [str(i.tag).split(',') for i in res]

variants = [' '.join(i) for i in variants]

for i in variants:
	print(i)