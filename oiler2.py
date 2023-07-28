def add_numbers(a, b):
    c = a + b
    b = d


"""
def add_fib(a,b):
    for i in range (1,10):
        c += b
# Example usage of the function:
result = add_numbers(5, 7)
print("Result:", result)  # Output: Result: 12
""" 
a = 1
b = 2
c = 3 
array = []
sum = 0
#def
while a < 4000000:
    c = a + b
    a = b
    b = c
    if (a % 2 == 0):
        array.append(a)
        
print(array)
    #print('a:' + str(a) + ' a:' + str(b))

for i in range(0, len(array)):
    sum = sum + array[i]
print(sum)

