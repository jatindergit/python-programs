class Human:
	def __init__(self,n,o):
		self.name = n
		self.occupation = o
		
	def do_work(self):
		if self.occupation == "designer":
			print(self.name, " do photoshop graphics")
		elif self.occupation == 'developer':
			print(self.name, " write complex codes to develop applications")
	
	def speek(self):
		print(self.name, ' says how are you doing?')
		
jatinder = Human('Jatinder', 'developer')
jatinder.do_work()
jatinder.speek()
	
