#input N
#for loop twice
#or while loop

#sol1
#hint
##N = int(input("N : "))
##
##i = 0
##while i<=9:
##    print("%d X %d = %d" %(N, i))
    
#sol2
N = int(input("N : "))
for i in range(2,N):
    for j in range(1,10):
        print(i*j, end= " ")
        
        
