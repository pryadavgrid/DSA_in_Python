# import array

#     * mean everything
from array import *


# array.array("TYPECODE", LIST-ITTRABLE_OF_INT)
# in the Typecode section basiclly we define that which type of element i want to store in my array eg. if we define int then we can't store any other datatype value like, str, float..etc
my_arr = array('i', [1,2,3,4,5])
my_char_arr = array('u', ['A','B','C','D'])

# retyrn Type of object
print(type(my_arr)) #<class 'array.array'>

# return array with 
print(my_arr)

for i in range(len(my_arr)):
    print(my_arr[i], end=",")

print()

for j in my_char_arr:
    print(j, end=" ")

print()

print("Type Code : ",my_char_arr.typecode)
print()

# reverse my arr
# my_char_arr.reverse() # modify the original array

# for i in my_char_arr:
#     print(i, end=" ")

# MY_ARR_OBJECT.insert('INDEX_NUMBER', 'VALUE')
# it not remove any element, it shift
my_char_arr.insert(1, 'O')
print(my_char_arr)

# insert any value in last 
my_char_arr.append('Z')
print(my_char_arr)

# when we want to replace any value to my previous array value
my_char_arr[2] = 'X'
print(my_char_arr)


my_copy_arr = array(my_arr.typecode, (i for i in my_arr))
# my_copy_arr = my_char_arr.copy()
print(my_copy_arr)

# Delete array element of given index or return remove element
# when we not give any index number then remove last element 
my_copy_arr.pop(1)
print(my_copy_arr)

# it remove the element if given value present in array
my_copy_arr.remove(4)
print(my_copy_arr)

# slishing 

my_new_arr = my_arr[2:4]
my_new_arr_2 = my_arr[2:-2]
my_rev_arr = my_arr[ : :-1]
print(my_new_arr)
print(my_new_arr_2)
print(my_rev_arr)