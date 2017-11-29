#Distionary
movie = {}

movie['IT'] = {
	'type' : 'Horror',
	'length' : 2.50,
	'rating' : '3/5'
}

movie['Criminal'] = {
	'type' : 'Action',
	'length' : 2.30,
	'rating' : '4/5'
}

import json
s = json.dumps(movie)
print(s)

with open('movies.txt','w') as f:
	f.write(s)
	
