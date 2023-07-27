###list+
##
##scores = [90, 80, 70, 60, 50]
##print(scores)
##average = sum(scores)/5
##print(average)

#range function -> make list
##a = list(range(1,10,1))
##print(a)
##b = list(range(5, 50,5))
##print(b)

#append function  shineer yum nemj oruulj boldog
##new_list  = [10, 20, 30]
##print(new_list)
##new_list.append(40)
##print(new_list)

#insert function(index) indexeer n orond n orluulj boldog
##a = [1,2,3,4,5]
##print(a)
##a.insert(1, 10)
##print(a)
##a.insert(2, "hello")
##print(a)

#extend function hoorond n zalgadag
##a = [1,2,3]
##b = [4,5,6]
##a.extend(b)
##print(a)
##print(b)

##a += [7,8,9] # a = a + [7,8,9]
##b -= [7,8,9] # b = b - [7,8,9]
##c *= [7,8,9] # c = c * [7,8,9]

#list and loop
##a = [1,2,3,4,5]
##i = 0
##
##while i<=4:
##     print(a[i])
##     i += 1
##
##print("\n")
##for n in a:
##    print(n)

##print(type(range(0,10)))
##print(range(10))
##print(range(2,10))
##print(list(range(10)))
##print(list(range(2,5)))
##print(list(range(-2,3)))
##print(list(range(3,2)))

#list input
##scores = []
##SUM = 0
##for i in range(5):
##    scores.append(int(input("scores input %d: " %(i+1))))
##    SUM += scores[i]
##    
##print(scores)
##print("sum: ", SUM)
##print("average: ", SUM/5)

#count function
##a = [10,20,20,40,50]
##print(a.count(10))
##print(a.count(20))

#remove function
##a = [10,20,30,40,50]
##print(a)
##a.remove(10)
##print(a)

#(index function
##a = [10,20,30,40,50]
##print(a.index(30))

#sort function bagaas n ih ruu erembeldeg
##a = [20,40,10,50,90,30]
##a.sort()
##print(a)

#pop function indexeer  haij boldog 
##a = [10,20,30,40,50]
##print(a.pop())
##print(a.pop())
##print(a.pop(0))

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end = " ")
    print()
              


           



