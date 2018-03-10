
array=[0,1,2,3,4,5]
#if array.__len__() == 0:
#    return 0
sum = 0
for i in range(0, array.__len__()):
    if i % 2 == 0 or i == 0:
        sum +=array[i]
        print(array[i])
        print(sum)
#print(sum)
sum = sum * array[-1]

print(sum)