

def insertion_sort(my_list):
    
    for i in range(1,len(my_list)):
        temp=my_list[i]
        j=i-1

        while temp < my_list[j] and j>-1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    
    return my_list


if __name__ == "__main__":
    print(insertion_sort([4,5,1,3,21,10,634,88,9,456,78,85,8,7,567,67,86,44,578,11,2234]))

