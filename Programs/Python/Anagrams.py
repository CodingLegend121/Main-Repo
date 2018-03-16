import itertools

word = str(input('Word:'))
word = list(word)
anagrams = ["".join(perm) for perm in itertools.permutations(word)]
anagrams = '\n'.join(map(str,anagrams))
print(anagrams)
