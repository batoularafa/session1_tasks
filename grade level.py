text = input("enter ur text:")
word = 1
sent = 0
letter = 0
#letter = len(text)

for i in text:
    if i == " ":
        word +=1
        
    if i == "." or i =="!":
        sent +=1
    
    if i.isalpha():
        letter+=1
        

avgletter = (letter/word)*100
avgsentence = (sent/word)*100
grade = 0.0588 * avgletter - 0.296 * avgsentence - 15.8

print(word, sent, letter)
print(avgletter, avgsentence, grade)

if grade >=16:
    print("Grade 16+")
elif grade <1:
    print("before grade 1")
else:
    print("grade", round(grade))
    
