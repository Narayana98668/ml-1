ages=[19,22,19,24,20,25,26,24,25,24] #sorting the list using sort function

ages.sort()

#finding minimum and maximum ages

a=min(ages)

b=max(ages)
print('min:',a)

print('max:',b)

print("sorted ages:",ages)

#adding minimum and maximum ages to the original List

ages.extend([a,b])

print("after adding min and max :",ages)