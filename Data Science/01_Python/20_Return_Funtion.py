

# def isPrime(user_input:int):
#     count = 0
#     prime= False
#     for i in range(2,int(user_input ** 0.5) + 1):
#         if(user_input % i ==  0):
#             return True
#         return False

# x = int(input('Enter a no :'))
# prime = isPrime(x)
# if (prime == True):
#     print("Prime no")
# else:
#     print("not a Prime no")



# def isPerfect(user_input:int):
#     total = 0
#     for i in range(1,user_input):
#         if(user_input % i  == 0):
#             total+=i

#     if (total == user_input):
#         return True
#     else:
#         return False
# x = int(input('Enter a no :'))
# perfect =isPerfect(x)
# if (perfect == True):
#     print("It is a perfect no")
# else:
#     print("It is not a perfect no")


# def isAmstrong(user_input:int):
#     digits= [int(d) for d in str(user_input)]
#     power = len(digits)
#     total  = sum(d**power for d in digits)
#     if total == user_input:
#         return True ,total
#     else:
#         return False ,total
        
# x = int(input('Enter a no :'))

# perfect,total =isAmstrong(x)
# if (perfect == True):
#     print(f"{x} is an Armstrong number.")
# else:
#     print(f"{x} is NOT an Armstrong number. (Sum is {total})")


# def isPelindrom(user_input:int):
#     real_value = user_input
#     revs = 0
#     while(user_input > 0):
#         last_digit = user_input % 10
#         revs = (revs*10) + last_digit
#         user_input = user_input // 10
    
#     print(revs)
#     if (real_value == revs):
#         print("It is a Pelindrom")
#     else:
#         print("It is not a Pelindrom")
# isPelindrom(int(121))

