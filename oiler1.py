#Loop through 1000
#if x / 3 | x / 5
#if x / 5
#append to array


array = []
sum = 0
#how to sum together array

for x in range(1, 1000):
  if x % 5 == 0 or x % 3 == 0:
    array.append(x)

for i in range(0, len(array)):
    sum = sum + array[i]

print(str(sum))
#print(5 % 5)

#how do i do this in javascript?