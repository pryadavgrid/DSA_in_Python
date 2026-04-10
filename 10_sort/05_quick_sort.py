# def quick_sort(my_list):

#     if len(my_list) <= 1:
#         return my_list
    
#     length_of_my_list = len(my_list)

#     pivot = my_list[0]

#     left_list = []
#     right_list = []


#     for i in range(length_of_my_list):
#         if my_list[i] > pivot :
#             right_list.append(my_list[i])
#         elif my_list[i] < pivot:
#             left_list.append(my_list[i])
#         else:
#             pass


#     return quick_sort(left_list) + [pivot] + quick_sort(right_list)



my_list = [20, 2, 9, 7, 12, 15, 1, 6 , 8]

# print(quick_sort(my_list))



def quick_sort_new(arr, left, right):
    
    if (left < right):

        p = partition(arr, left, right)

        quick_sort_new(arr, left, p-1)
        quick_sort_new(arr, p+1, right)

def partition(arr, left, right):
    pivot = arr[left]
    i = left + 1
    j = right

    while True:

        while(i<j and arr[i] < pivot):
            i = i + 1

        while (i < j and arr[i] > pivot):
            j = j - 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else: 
            break

    arr[left], arr[j] = arr[j], arr[left]

    return j


quick_sort_new(my_list, 0, len(my_list) - 1 )

print(my_list)