# dict testing...

import sys

#dict1={'symbol':'AAPL','shares':'2000'}
#print dict1

#for k,v in dict1():
#	print (k)

#sys.exit(0)

#    output_dict[x] = output


cars = {'A':{'speed':70, 'color':2},
        'B':{'speed':60, 'color':3}}

for x in cars:
    print (x)
    for y in cars[x]:
#        print (y,':',cars[x][y])
	print (y),
#	print (y,cars[x][y])
	print (cars[x][y])
