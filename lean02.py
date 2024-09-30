

#12.65 Input fine tuple
tuple1 = (x for x in range(1,10))
input_num = int(input("number :"))
if input_num in tuple1:
    print("Yes")
else:
    print("No")
