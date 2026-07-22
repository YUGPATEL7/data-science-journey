# def Sigma(user_input:int):
#     total = 0
#     for i in range(1,user_input+1,1):
#         total+=i
#         print(i,end=" + ")

#     print("\b\b=",total)
    
# x = int(input('Enter a no :'))
# Sigma(x)


# def isPrime(user_input:int):
#     count = 0
#     for i in range(2,int(user_input ** 0.5) + 1):
#         if(user_input % i ==  0):
#             print("not a Prime no")
#             return
#     print("not a Prime no")

# x = int(input('Enter a no :'))
# isPrime(x)



# def isPerfect(user_input:int):
#     total = 0
#     for i in range(1,user_input):
#         if(user_input % i  == 0):
#             total+=i

#     if (total == user_input):
#         print("It is a perfect no")
#     else:
#         print("It is not a perfect no")
# x = int(input('Enter a no :'))
# isPerfect(x)


# def isAmstrong(user_input:int):
#     digits= [int(d) for d in str(user_input)]
#     power = len(digits)
#     total  = sum(d**power for d in digits)
#     if total == user_input:
#         print(f"{user_input} is an Armstrong number.")
#     else:
#         print(f"{user_input} is NOT an Armstrong number. (Sum is {total})")
# x = int(input('Enter a no :'))
# isAmstrong(x)

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

