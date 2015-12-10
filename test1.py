import sys

try:
	s=raw_input('Enter something -->')
except NameError:
	print('\nWhy did you do a wrong name on me?')
	sys.exit()
print('Done')