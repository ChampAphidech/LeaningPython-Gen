

# #12.65 Input fine tuple
# tuple1 = (x for x in range(1,10))
# input_num = int(input("number :"))
# if input_num in tuple1:
#     print("Yes")
# else:
#     print("No")

#12.66 len tuple
tuple1 = tuple([x for x in range(1,10)])
input_num = int(input("number :"))
if input_num > len(tuple1):
    print("input more than len")
elif input_num < len(tuple1): 
    print("input less than len")
else :
    print("Is equal")