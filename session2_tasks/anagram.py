def anagram(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    for i in str1:
        if (i in str2) and (len1 == len2):
            flag = 0
        else:
            flag = 1
            break
    if flag == 1:
        print("not anagram")
    else: 
        print("anagram")

anagram("hello", "lelhoo")