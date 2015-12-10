class SIException(Exception):
	def __init__(self,length,atleast):
		Exception.__init__(self)
		self.length=length
		self.atleast=atleast

try:
	s=input("Enter Something -->")
	if len(s)<3:
		raise SIException(len(s),3)
except EOFError:
	print('\nWhy did you do an EOF on me?')
except SIException:
	print('SIException:The input was of length %d,was exceptting at least %d'%(SIException.length,SIException.atleast))
else:
	print('NO Exception was raised.')