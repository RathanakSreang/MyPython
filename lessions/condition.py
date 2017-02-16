num = 1
if num < 1:
    print("Number is lessthan 0")
elif(num == 1):
   print("Number is equal 1")
else:
   print("Number is grater than 1")
x = int(input("Please enter number: "))
if x < 0:
    print("Negative chnged to zero")
    x = 0
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('Plural')
