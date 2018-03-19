import itertools


def generator(word):
	word = word.lower()
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
def checker(checkString):
	firstString,secondString = checkString.split(',')
	firstString = sorted(list(firstString.lower()))
	secondString = sorted(list(secondString.lower()))
	if firstString == secondString:
		print('They are anagrams')
	else:
		print('They are not anagrams')
		
		
anagramType = input('Check or Generate [c/g]')
if anagramType == 'c':
	wordC = input('Type two words using a comma to separate : ')
	print('\n')
	checker(wordC)
elif anagramType == 'g':
	wordG = input('Word [ 2-5 letters recommended ] : ')
	print('\n')
	generator(wordG)
