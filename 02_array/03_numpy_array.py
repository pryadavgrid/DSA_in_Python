import numpy as np
from numpy import *

# why we use numpy array : numpy provide us create a hartoginiuos array mean we can store any type of element (int, char, float, bool etc.)
# if we want to store same datatype value then we need to give datatype
# np.array(LIST, DATATYPE)

# hetroginiuos
my_numpy_arr = array([1,'A',3.4,True])
# print(my_numpy_arr)

# float datatype
my_numpy_float_arr = array([1,2,3,4], float)
# print(my_numpy_float_arr)


# linspace(start_number, end_number, How_many_partition)
my_linespase_arr = linspace(10, 100, 10, dtype=int)
# print(my_linespase_arr)


# arange(start,stop,step)
my_arrange_arr = arange(10,20,2)
# print(my_arrange_arr)

# zeros(size_of_arr, datatype)
my_zero_arr = zeros(10, int)
# print(my_zero_arr)

my_one_arr = ones(10, int)
# print(my_one_arr)

# when we want a specific value of array
# full(size_of_arr, value_you_to_fill, datatype)
my_specific_arr = full(10, 5,int)
# print(my_specific_arr)




# Multidimentional Array
my_array = array(10)
# print(my_array)

one_dimen = array([1,2,3,4])
# print(one_dimen)

two_dimen = array([[1,2,3,4],[5,6,7,8],[9,0,10,11]])
# print(two_dimen)

three_dimen = array([  [ [1,3],[2,3] ],  [ [4,5],[5,6] ],  [ [7,8],[9,0] ] ])
print(three_dimen)