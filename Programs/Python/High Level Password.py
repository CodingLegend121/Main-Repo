import hashlib
from termcolor import colored
from replit import clear
clear()
def passw(Password,Attempt):
	passcode = Password[::-1]
	def md5(string):
	  return hashlib.md5(bytes(string, "utf-8")).hexdigest()
	pw = md5(input('\nPasscode:'))
	x=1
	while pw!=passcode and x < Attempt:
		print(colored('\nIncorrect Password Attempt ' + str(x) + '\n','red'))
		pw = md5(input('Passcode:'))
		x += 1
	if passcode!=pw:
		print(colored('\nYou have used your ' + str(Attempt) + ' Attempts','red',attrs=['bold']))
	else:
		print(colored('\nPasscode Matches\n','green',attrs=['blink']))

passw('9787dd6d451a51328a96bb480cf122e4',2)
