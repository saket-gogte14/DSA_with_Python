
def items_in_common(list1, list2):
    common_items=[]

    for item in list1:
        if item in list2:
            return True

    return common_items

if __name__ == '__main__':
    list1=[1,4,5]
    list2=[6,5,7]

    print(items_in_common(list1,list2))


