
def items_in_common(list1, list2):
    common_items=[]

    for item in list1:
        if item in list2:
            common_items.append(item)

    return common_items

if __name__ == '__main__':
    list1=[1,4,5,8,9,10,44,77]
    list2=[6,5,7,6,7,8,9,10,44,5,6,7,898]

    print(items_in_common(list1,list2))


