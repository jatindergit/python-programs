movies = [
			'Titanic',[
				'Amy Virk',[
					'Chaca','Chore'
					]
				], 
			'London Has Fallen',[
				'Nerru Bajva',[
					'Mandy takkar'
					]
				]
		]	

for movie in movies:
	if isinstance(movie,list):
		for nest_movie in movie:
			print(nest_movie)
	else:
		print(movie);

