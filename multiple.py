class Father:
	def __init__(self):
		print("Father's init")
		
	def skills(self):
		print("Gym, Programming, Watch movies")
		
class Mother:
	def __init__(self):
		print("Mother's init")
		
	def skills(self):
		print("art, Cooking")
		
class Kid(Mother, Mother,Father, Father):
	#def __init__(self):
	#	print("kid's init")
		
	def skills(self):
		print('sports')
		
		
k = Kid()
k.skills()
dir(k)
