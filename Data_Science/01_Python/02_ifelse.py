# # 1 marksheet
# print("1.\nMarksheet")
# m1=int(input("Enter Maths Marks:"))
# m2=int(input("Enter Science Marks:"))
# m3=int(input("Enter Hindi Marks:"))
# m4=int(input("Enter Gujrati Marks:"))
# m5=int(input("Enter English Marks:"))


# if m1 > 100 or m2 > 100 or m3 > 100 or m4 > 100 or m5 > 100:
#     print("ohe marks 100 ye 100 se andre enter kar :) ")
    
# else:
#     total=m1+m2+m3+m4+m5
#     per=total/5
#     Grade='N/A'
#     if(per <=35):
#         Grade ='F'
#         print("Fail")
#     elif(per < 40):
#         Grade ='E'
        
#     elif(per < 50):
#         Grade ='D'
        
#     elif(per < 60):
#         Grade ='C'
        
#     elif(per < 70):
#         Grade ='B'
        
#     else:
#         Grade ='A'
        
#     print("Total : ",total)
#     print("Per : ",per)
#     print("Grade : ",Grade)


# # 2 Age Calc
# age = int(input("Enter your age (Year) :- "))

# Month = age*12
# print("Month: ",Month)

# days=age*356
# print("Days:",days)

# week =round(days/7)
# print("Week: ",week)

# hours = days*24
# print("Hours:",hours)

# min= hours*60
# print("Minutes:",min)

# sec = min*60
# print("Seconds:",sec)


# # Shopping

# Customer = input("Enter your name: ")
# Product = input("Enter Product name: ")
# Price = int(input("Enter Price: "))
# Qty =int(input("Enter Product Qty: "))


# Total = Price*Qty
# Discount = 2/100
# Net_Total = 0

# if(Total >= 1500):
#     Discount =15 /100
# elif Total >=1000:
#     Discount =10 /100
# elif Total>= 500:
#     Discount=5 /100

# Discount =Total * Discount
# Net_Total=Total- Discount

# print("Total ",Total)
# print("Discount ",Discount)
# print("Net Total ",Net_Total)

# print ("Tx... ",Customer," For Shopping ",Product)

##4. Min /Max

# Num1 = int(input("Enter 1st Number: "))  
# Num2 = int(input("Enter 2st Number: "))  

# if(Num1==Num2):
#     print("Both are Same")
# elif (Num1 > Num2):
#     print(f"{Num1} is Max Then {Num2}")
# else:
#     print(f"{Num1} is Min Then {Num2}")


##5. 3no. Min /Max

# Num1 = int(input("Enter 1st Number: "))  
# Num2 = int(input("Enter 2st Number: "))  
# Num3 = int(input("Enter 3st Number: "))  

# if(Num1== Num2 ==Num3 ):
#     print("All 3 are Same")
# elif (Num1 > Num2 and Num1> Num3):
#     print(f"{Num1} is Max Then {Num2} and {Num3}")
# elif (Num2 > Num1 and Num2> Num3):
#     print(f"{Num2} is Max Then {Num1} and {Num3}")

# else:
#     print(f"{Num3} is Max Then {Num1} and {Num2}")
    

## 6 Pos+ / Neg-

# num = int(input('Enter a No. '))

# if(num < 0):
#     print(num,"is Negative")
# else:
#     print(num,"is Postive")

## 7 odd/even 

# num = int(input('Enter a No. '))

# if(num % 2 == 0):
#     print(num,"is Even")
# else:
#     print(num,"is Odd")


## 8 Divide by 3 & 7 

# num = int(input('Enter a No. '))

# if(num % 3 == 0 and num % 7  == 0 ):
#     print(num,"is Divide by 3 & 7")
# else:
#     print(num,"is not Divide by 3 & 7")

## 9 Calc

# num1 = int(input('Enter a 1st no'))
# num2 = int(input('Enter a 2st no'))

# opration = int(input('Enter you \n1 -> + \n2 -> - \n3 -> * \n4 -> / '))

# if (opration == 1):
#     print("Sum ",num1+num2)
# elif(opration == 2):
#     print("Sub ",num1-num2)
# elif(opration == 3):
#     print("Mul ",num1*num2)
# elif(opration == 4):
#     if(num1 <= 0 ):
#         print("Enter apart form zero")
#     else:
#         print("Div ",num1/num2)
# else:
#     print("Invalid option ")


##10 Convertor


# opration = int(input('Enter you \n1 -> $ to Rs  \n2 -> Rs to $  \n3 -> kg to pound  \n4 -> pound to kg \n5 -> m to cm \n6 -> cm to m \n7 -> Ferenhit to Celcius \n8 -> Celcius to ferenhit \n9 -> Km to m '))
# num1 = int(input('Enter a 1st no'))

# if (opration == 1):
#     print("Rupee",num1 * 95)
# elif(opration == 2):
#     print("Doller ",num1 / 95)
# elif(opration == 3):
#     print("Pound  ",num1*2.2)
# elif(opration == 4):
#         print("Kg  ",num1 / 2.2)
# elif(opration == 5):
#         print("cm ",num1 *100)
# elif(opration == 6):
#         print("m ",num1 / 100)
# elif(opration == 7):
#         print("Celcius ",(5/9)*(num1-32))
# elif(opration == 8):
#         print("ferenhit ",((9*num1)/5)+32)
# elif(opration == 9):
#         print("m ",num1 * 1000)
# else:
#     print("Invalid option ")


## 12 Simple Ques 

# print("5 X 2 = ? ")
# print("a.8 b.9 c.10 d.11")
# user_input =input("Enter your ans ")
# if (user_input  == "a"):
#     print("8 is Worng Ans")
# elif(user_input =="b"):
#     print("9 is Worng Ans")
# elif(user_input =="c"):
#     print("10 is Correct ans ")
# elif(user_input =="d"):
#     print("11 is Worng Ans")

## 13 

print("5 X 2 = ? ")
print("a.8 b.9 c.10 d.Skip")
user_input =input("Enter your ans ")
attempt = 0
skip = 0
right = 0
wrong = 0
marks = 0
cut_marks = 0
result = 0

if (user_input  == "c"):
    print("10 is correct Ans")
    attempt+=1
    right+=1
    marks=+10
elif(user_input  == "d"):
    print("Skip this ques")
    skip+=1
else:
    print("Worng Ans")
    wrong+=1
    cut_marks+=10

result = marks - cut_marks
print("Attempt :", attempt)
print("Right   :", right)
print("Wrong   :", wrong)
print("Skip    :", skip)
print("Marks   :", marks)
print("Cut     :", cut_marks)
print("Result  :", result)


## 14 