## While Loop 

# while user_input > 0: ture (then only move inside)
#     print(user_input)
#     user_input-=1

## 1 1 to n number 

# user_input = int(input('Enter a No. '))
# a =1
# while a <= user_input:
#     print(a)
#     a+=1

## 2 n number to 1 

# user_input = int(input('Enter a No. '))
# while user_input > 0:
#     print(user_input)
#     user_input-=1

## 3 n1 to n2 

# user_input1 = int(input('Enter a No. '))
# user_input2 = int(input('Enter a No. '))
# while user_input2 > user_input1:
#     print(user_input1)
#     user_input1+=1


##4  Sigma 

# user_input1 = int(input('Enter a No. '))
# sum =0
# while user_input1 > 0:
#     sum += user_input1 
#     user_input1-=1
#     print(sum)

##5  Factorial

# user_input1 = int(input('Enter a No. '))
# sum =1
# while user_input1 > 0:
#     sum *= user_input1 
#     user_input1-=1

# print(sum)

##6 Even / odd 

# user_input1 = int(input('Enter a No. '))
# i=0
# print("Even:-",end="")

# while (i <=user_input1):
#     if i % 2 == 0:
#         print(i,end=",")
#     i+=2

# print()
# i=1
# print("Odd:-",end="")
# while (i <=user_input1):
#     if i % 2 != 0:
#         print(i,end=",")
#     i+=2


## 7 Even/ odd in 1 loop 

# user_input1 = int(input('Enter a No. '))
# i=1
# print("Odd Even",end="\n")

# while(i <= user_input1):
#     if(i%2 != 0):
#         print(i,end="\t")
#     else:
#         print(i)
#         print()
#     i+=1

## 8 3 & 7 = 21,42,84,......


# user_input1 = int(input('Enter a No. '))
# i=1
# print("3 & 7 :- ",end="")

# while(i <= user_input1):
#     if(i%3 == 0 and i%7==0):
#         print(i,end="\t")
        
#     i+=1

## 10 Multiplication Table

# user_input1 = int(input('Enter a No. '))
# i=1
# while(i<= 10):
#     print(f"{user_input1} X {i} = {user_input1*i} ")
#     i+=1

## 11 Multi Multiplication Table

# user_input1 = int(input('Enter a No. '))
# user_input2 = int(input('Enter a No. '))
# i=1
# while(i<= 11 and user_input1 <= user_input2):
#     if(i <= 10):
#         print(f"{user_input1} X {i} = {user_input1*i} ")
#         i+=1
#     else:   
#         user_input1+=1
#         i=1

##12 Prime no

# user_input = int(input('Enter a No' ))

# i=1
# count=0
# while (i <= user_input):
#     if (user_input  % i ==0):
#         count+=1
#     i+=1

# if(count == 2):
#     print("Prime no ")
# else:
#     print("Not a prime no ")


## 13 Perfect No :- 6 (1, 2, 3,  4 , 5) (1 + 2 + 3 = 6)

# user_input = int(input('Enter a No' ))

# i=1
# a=0
# while (i <= user_input or user_input == a ):
#     print (i,"+ ",end="")
#     i+=1
#     a+=i

# print("=",a)

## 16 Reverse No 

user_input = int(input('Enter a No' ))
a= 0
while (user_input > 0 ):
    user_input = user_input % 10
    user_input/=10
    user_input = () 
    print(a)
