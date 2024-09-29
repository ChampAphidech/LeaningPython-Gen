#Tuple + if-else + loop
#12.60 
# list1 = ['a','b','c','d','e','f']
# tuple1 = tuple(list1)
# print(tuple1)

#12.61
sumx=0
tuple1 = tuple(x for x in range(1,11))
n_tuple1 = len(tuple1)
for i in range(n_tuple1):
    if(i%2==0):
        sumx = sumx + tuple1[i]**2
print(sumx)