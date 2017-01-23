# dict testing...
import sys

cars = {'mustang':{'speed':170, 'model':'shelby'},
        'camaro':{'speed':190, 'model':'ss'}}

print "---------"

for k in cars:
	k2=cars.get(k)
	print (k2.values())
	for z in (k2.values()):
		print (z),

print
print "---------"

# Good example:
for x in cars:
    print (x),
    for y in cars[x]:
	print (y),
	print (cars[x][y]),
    print

# Good example2:
print "---------"
for x in cars:
    for y in cars[x]:
        print (cars[x][y]),
	print ('|'),
    print

