value = int(input("enter amount:"))
twohundred = 0
hundred = 0
fifty = 0
twenty =0
ten = 0
five = 0 
one = 0
if (value/200)>0:
    twohundred = value//200
    new_val = value - (twohundred*200)
if(new_val/100)>0:
    hundred = new_val//100
    new_val = new_val - (hundred*100)
if(new_val/50)>0:
    fifty = new_val//50
    new_val = new_val - (fifty*50)
if(new_val/20)>0:
    twenty = new_val//20
    new_val = new_val - (twenty*20)
if(new_val/10)>0:
    ten = new_val//10
    new_val = new_val - (ten*10)
if(new_val/5)>0:
    five = new_val//5
    new_val = new_val - (five*5)
if(new_val/1)>0:
    one = new_val//1
    new_val = new_val - (one*1)

print(twohundred,"x 200 L.E. + ", hundred,"x 100 L.E. + ", fifty,"x 50 L.E. + ", twenty,"x 20 L.E. + ", ten,"x 10 L.E. + ", five,"x 5 L.E. + ", one,"x 1 L.E.")