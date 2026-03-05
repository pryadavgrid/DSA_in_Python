from array import *

# my_arr = array('i', [])
my_arr = array('i', [1,2,3,4,5,6,7,8,9])

# range_input = int(input("Enter a range : "))

# for num in range(range_input):
#     my_arr.append(int(input('Enter a number : ')))

# print(my_arr)

# when we want to know any value present in array if present then what is index 
input_value = int(input('Enter a number : '))
try:
    index_of_val = my_arr.index(input_value)
except Exception as e:
    print(e)
else:
    print(f"Index is : {index_of_val}")