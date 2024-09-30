#Tuple + if-else + loop
#12.60 
# list1 = ['a','b','c','d','e','f']
# tuple1 = tuple(list1)
# print(tuple1)

#12.61
# sumx=0
# tuple1 = tuple(x for x in range(1,11))
# n_tuple1 = len(tuple1)
# for i in range(n_tuple1):
#     if(i%2==0):
#         sumx = sumx + tuple1[i]**2
# print(sumx)

#12.62
# sumx=0
# tuple1 = tuple(x for x in range(1,11))
# n_tuple1 = len(tuple1)
# for i in range(n_tuple1):
#     if(i%2==1):
#         sumx = sumx + tuple1[i]**2
# print(sumx)

#12.63 Prime Number in tuple
# tuple1 = (x for x in range(1,26))
# # print(tuple1)
# for num in tuple1:
#     count=0
#     for i in range(1,num+1):
#         # print(num,i)
#         if (num%i==0):
#             count = count +1
            
#     if(count==2):
#         print(num)
        
#12.64 meanx. Number prime in tuple
tuple1 = (x for x in range(1,26))
sumx = 0
count_prime = 0
# print(tuple1)
for num in tuple1:
    count=0
    for i in range(1,num+1):
        # print(num,i)
        if (num%i==0):
            count = count +1
            
    if(count==2):
        # print(num)
        sumx = sumx + num
        count_prime = count_prime+1
meanx = sumx / count_prime
print(meanx)