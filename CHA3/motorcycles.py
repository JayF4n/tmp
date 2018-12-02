motorcycles = ['honda','yamaha','suzuki']

print(motorcycles)

motorcycles[0] = 'ducati'

print(motorcycles)

motorcycles.append('honda')

print(motorcycles)

motorcycles = []

motorcycles.append('honda')

motorcycles.append('yamaha')

motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0,'ducati')

print(motorcycles)

del motorcycles[0]

print(motorcycles)

popped_motorcycles = motorcycles.pop()

print(motorcycles)

print(popped_motorcycles)

motorcycles.insert(2,popped_motorcycles)

print(motorcycles)

first_owned = motorcycles.pop(0)

print("The first motorcycle I owned was a " + first_owned)

motorcycles.insert(0,'ducati')

print(motorcycles)

too_expensive = 'ducati'

motorcycles.remove(too_expensive)

print(motorcycles)

print("\nA " + too_expensive.title() + " is too expensive.")