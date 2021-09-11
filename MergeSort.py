

def Merge(list1, list2):
    merged_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1 
        else:
            merged_list.append(list2[j])
            j += 1 
        
        #print (i, j)

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list

def MergeSort(my_list):
    if len(my_list) == 1:
        return my_list
    
    mid = int(len(my_list) / 2)
    left = my_list[:mid]
    right = my_list[mid:]

    return (Merge(MergeSort(left),MergeSort(right)))

print(MergeSort([4,5,6,78,1,2,155,600,890,999,1023]))
