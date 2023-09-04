def count_sort(array):
    max = 0
    for i in array:
        if i>max:
            max =i

    count = [0]*(max+1)
    for i in array:
        count[i]+=1

    for i in range(1, len(count)):
        count[i]+=count[i-1]

    sorted_lst=[0]*(len(array))
    for i in range(len(array)-1, -1, -1):
        num = array[i]
        ind = count[num]-1
        sorted_lst[ind]= num
        count[num] -=1
    return sorted_lst




lst = [25, 6, 1, 269, 58, 7]
print(count_sort(lst))

