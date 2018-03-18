import itertools
from time import sleep

word = input('Word:').lower()
word = list(str(word))
anagrams = ["".join(perm) for perm in itertools.permutations(word)]
file = open('wordlist.txt', 'r')
lines = file.read().split('\n')
for n, i in enumerate(anagrams):
			if i not in lines:
    				anagrams[n] = ''
anagrams = '\n'.join(map(str,anagrams))
print(anagrams.strip(''))
sleep(100)
