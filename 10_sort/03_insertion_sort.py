def insertion_sort(my_list):
    length_of_my_list = len(my_list)
    for i in range(1 , length_of_my_list):

        initial_value = i

        while ( (my_list[initial_value] < my_list[initial_value - 1]) and (length_of_my_list > initial_value > 0) ):
            my_list[initial_value], my_list[initial_value-1] = my_list[initial_value-1], my_list[initial_value]
            initial_value = initial_value - 1



    return my_list



my_list = [64,25,32,20,40,15]
sorted_list_using_insertion_sort = insertion_sort(my_list)
print(sorted_list_using_insertion_sort)





