import sys

def StairCase(n):
    mynum = n
    while ((mynum < 1) or (mynum > 100)):
        try:
            mynum = input('Enter a number between 1 and 100: ')
        except:
            print ("Must enter an integer only!")
    spaces=n-1
    while (spaces >= 0):
        for x in xrange(0,spaces):
            sys.stdout.write(' ')
        for w in xrange(0,(n-spaces)):
            sys.stdout.write('#')
        spaces -= 1
        print
    return

while True:
 try:
      mynum0=input('First enter a number between 1 and 100: ')
      StairCase(mynum0)
 except:
      print ("First Must enter an integer only!")

sys.exit(0)