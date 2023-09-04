num = int(input("enter credit card number:"))
digits = []
digitmultiples = []
while num > 0:
    mdul = num % 10
    num = num //10
    digits.append(mdul)

for i in range(0, len(digits)):
    if i%2 != 0:
        mult = 2*digits[i]
        while mult > 0:
            newmult = mult % 10
            mult = mult//10
            digitmultiples.append(newmult)

sum1=0
sum2=0
for i in digitmultiples:
    sum1 += i
for i in range(0, len(digits)):
    if i%2 == 0:
        sum2 += digits[i]

totalsum = sum1 + sum2
totalsum_string = str(totalsum)
index = len(totalsum_string)-1
checksum = totalsum_string[index]

#print(digits, digitmultiples, sum1 , sum2, totalsum, checksum)


if checksum=='0' :
    if (digits[-1] == 3)  and ((digits[-2] == 4) or (digits[-2] == 7)) :
        print("American Express")
    elif (digits[-1] == 5)  and ((digits[-2] == 1) or (digits[-2] == 2) or (digits[-2] == 3) or (digits[-2] == 4) or (digits[-2] == 5)):
        print("mastecard")
    elif (digits[-1] == 4) :
        print("visa")
else:
    print("invalid")



