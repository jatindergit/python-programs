def generate_next():
    yield "a"
    yield "b"


itr = generate_next()
try:
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
except Exception as e:
    print(e)

for c in generate_next():
    print(c)
