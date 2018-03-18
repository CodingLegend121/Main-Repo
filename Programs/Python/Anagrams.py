#import itertools
#from termcolor import colored


word ='what'
#'''input('Word:').lower()'''
#word = list(str(word))
'''
anagrams = ["".join(perm) for perm in itertools.permutations(word)]
anagrams = '\n'.join(map(str,anagrams))'''
file = open('wordlist.txt', 'r')
lines = file.read().split('\n')
'''if anagrams[] in lines:
	print(colored(anagrams,'green'))
else:
	print(colored(anagrams,'red'))
	'''
if word in lines:
	print('Noice')
else:
	print('You suck')
