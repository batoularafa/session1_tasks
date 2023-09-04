def sum_in_list(array, num):
    i = 0
    for x in array:
        if x>num:
            del x

    if i == (len(array)):
        return "no"
    for j in range(i, len(array)):
        if (array[i] + array[j]) == num:
            return f"yes, {array[i]} + {array[j]} = {num}"
        
    del array[i]
    return sum_in_list(array, num)
        
lst= [43, 23, 79, 54, 17, 16]
print(sum_in_list(lst, 40))