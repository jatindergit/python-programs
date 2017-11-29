#example of list
prime_numbers = [2, 3, 5, 7, 11, 13, 17]
print("Type of prime_number: ", type(prime_numbers)) #Output: Type of prime_number:  <class 'list'>

#example of tuple
even_numbers = 2, 4, 6, 8, 10, 12, 14
print("Type of even_numbers: ", type(even_numbers)) #Output: Type of even_numbers:  <class 'tuple'>
#OR
odd_numbers = (1, 3, 5, 7, 9, 11, 13)
print("Type of odd_numbers: ", type(odd_numbers)) #Output: Type of odd_numbers:  <class 'tuple'>

# Loop over prime_numbers
print("List of prime numbers:")
for prime_num in prime_numbers:
    print(prime_num)

# Loop over even_numbers
print("List of even numbers:")
for even_num in even_numbers:
    print(even_num);

# Loop over odd_numbers
print("List of odd numbers:")
for odd_num in odd_numbers:
    print(odd_num);

print("List Methods:")
print(dir(prime_numbers))
print("-"*80);

print('Tuple Methods:')
print(dir(even_numbers))




name , age = ['jazz', 24]
print(name)
print(age)

name, age = ('Gur', 23)
print(name)
print(age)

empty_tuple = ()
test1 = ("a")
test2 = ("a","b")
test3 = ("a","b","c")
print(empty_tuple)
print(test1)
print(test2)
print(test3)


name, age, city = ('Jazz', 24,'San Diago')
print("Name: ",name)
print("Age: ",age)
print("City: ",city)


country = ('US')
print(type(country))
