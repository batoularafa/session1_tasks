def balanced_br(str):
    count = 0
    for i in str:
        if i == '(':
            count +=1
        elif (i == ')') and (count > 0):
            count -=1
    if count == 0:
        return "balanced brackets"
    else:
        return "unbalanced brackets"
    

brack = ")("
print(balanced_br(brack))
