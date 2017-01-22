#
import sys

def StairCase(n):
    mynum = n
    while ((mynum < 1) or (mynum > 100)):
        try:
            mynum = input('Enter a number between 1 and 100: ')
        except:
            print ("Enter an integer only!")

    spaces=mynum-1
    while (spaces >= 0):
        for x in xrange(0,spaces):
            sys.stdout.write(' ')
        for w in xrange(0,(mynum-spaces)):
            sys.stdout.write('#')
        spaces -= 1
        print
    return

# MAIN

while True:
 try:
      mynum0=input('First enter a number between 1 and 100: ')
      StairCase(mynum0)
 except:
      print ("Enter an integer only!")

sys.exit(0)
