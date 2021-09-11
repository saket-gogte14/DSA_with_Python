
def swap(my_list, index1, index2):
        temp = my_list[index1]
        my_list[index1] = my_list[index2]
        my_list[index2] = temp

        return my_list

def pivot(my_list, pivot_index, end_index):
    swap_index=pivot_index
    
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            my_list = swap(my_list, swap_index, i)
        
    my_list = swap(my_list, pivot_index, swap_index)

    return swap_index

def quick_sort(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort(my_list, left, pivot_index - 1)
        quick_sort(my_list, pivot_index + 1, right)
    
    return my_list 

list_to_sort = [4,5,1,3,21,10,634,88,9,456,78,85,8,7,567,67,86,44,578,11,2234]
print(quick_sort(list_to_sort,0,len(list_to_sort)-1))


