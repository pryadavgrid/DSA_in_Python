def devide_arr(my_list, left, right):
    if left < right:
        middle = (left + right) // 2 
        devide_arr(my_list, left, middle)
        devide_arr(my_list, (middle + 1), right)
        merge_sort(my_list,left, middle, right)



def merge_sort(my_list, left, middle, right):
    s1 = middle - left + 1
    s2 = right - middle

    left_arr = [0] * s1
    right_arr = [0] * s2

    for i in range(s1):
        left_arr[i] = my_list[left + i]

    for j in range(s2):
        right_arr[j] = my_list[middle + 1 + j]


    i = j = 0
    k = left

    while i < s1 and j < s2:
        if(left_arr[i] < right_arr[j]):
            my_list[k] = left_arr[i]
            i = i + 1
            k = k + 1
        else:
            my_list[k] = right_arr[j]
            j = j + 1
            k = k + 1
    
    while i < s1 :
        my_list[k] = left_arr[i]
        i = i + 1
        k = k + 1

    while j < s2:
        my_list[k] = right_arr[j]
        j = j + 1
        k = k + 1
    




my_list = [2,10,5,4,18,15,1]
devide_arr(my_list, 0, len(my_list) - 1)
print(my_list)
# sorted_array_using_merge_sort = merge_sort(my_list)
# print(sorted_array_using_merge_sort)