# dict testing...

import sys

#dict1={'symbol':'AAPL','shares':'2000'}
#print dict1
#for k,v in dict1():
#	print (k)
#sys.exit(0)
#    output_dict[x] = output
#########

cars = {'mustang':{'speed':170, 'model':'shelby'},
        'camaro':{'speed':190, 'model':'ss'}}

print "---------"

for k in cars:
	k2=cars.get(k)
	print (k2.values())
	for z in (k2.values()):
		print (z),

#	for z in cars.k.get(k2):
#		print (z)

#	print (k),
#	print dict.values(dict.values(cars))
#	print dict.get(cars, default=None)

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








#	print (y,cars[x][y])
#        print (y,':',cars[x][y])
