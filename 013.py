##import random
##import time
##
##print("dice")
##
##while 1:
##    value = random.randint(1,6)
##    print("dice value: %d" %value)
##    time.sleep(2)
##sys.exit()

#range
#example
#start = 1
#end : input
#num count -> use while loop

#hint
##import random
##import time
##startvalue = int(input("startvalue: "))
##endvalue = int(input("endvalue: "))

##while startvalue <= endvalue:
##    print("count: %d" %startvalue)
##    startvalue += 1

##for startvalue in range(startvalue, endvalue+1, 1):
  ##  print("count: %d" % startvalue)
##
##oroltiin m utgiig n oroltiin utga deer nemeed tedgeeriin niilberiig hevlene
import sys
startvalue = int(input("startvalue: "))
endvalue = int(input("endvalue: "))
SUM = 0

# hint : sys.exit()

if(startvalue <= endvalue):
    while startvalue <= endvalue:
        print("count: %d: " %startvalue)
        SUM += startvalue
        startvalue += 1    
else:
    sys.exit()
print(SUM)
    

    
print(SUM)
          

##
##a = [1,2,3,4,5,6]
##for i in a:
##    if i > 3:
##        break
##    print(i)
##

   
