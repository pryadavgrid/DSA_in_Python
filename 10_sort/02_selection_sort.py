def selection_sort(my_list):
    length_of_my_list = len(my_list)
    # min_element = my_list[0]

    for i in range(length_of_my_list):
        min_element = my_list[i]
        index = i
        for j in range( i + 1 , length_of_my_list):
            if my_list[j] < min_element:
                min_element = my_list[j]
                index = j
        
        my_list[i], my_list[index] = my_list[index], my_list[i]

    return my_list





my_list = [64,25,32,20,40,15]

my_sorted_list_using_selection_sort = selection_sort(my_list)
print(my_sorted_list_using_selection_sort)