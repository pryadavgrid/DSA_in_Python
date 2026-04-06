def bubble_sort(my_list):

    length_of_list = len(my_list)

    for i in range(1, length_of_list):
        for j in range(0, length_of_list - i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]


    return my_list


my_list = [64,32,25,45,20,15, 80, 30]

my_sorted_list_using_bubble_sort = bubble_sort(my_list)
print(my_sorted_list_using_bubble_sort)