import itertools
word = input('Word [ 2-5 letters recommended ] :').lower()
word = list(str(word))
anagrams = ["".join(perm) for perm in itertools.permutations(word)]
file = open('wordlist.txt', 'r')
lines = file.read().split('\n')
for n, i in enumerate(anagrams):
			if i not in lines:
        			anagrams[n] = '/'
if str('/') in anagrams:
	anagrams = [x for x in anagrams if x != '/']
			
anagrams = '\n'.join(map(str,anagrams))
print(anagrams)
