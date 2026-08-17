# def Sigma():
#     user_input = int(input('Enter a no: '))
#     total = 0
#     for i in range(1,user_input+1,1):
#         total+=i
#         print(i,end=" + ")

#     print("\b\b=",total)
    
# Sigma()

    
# def Factorial():
#     user_input = int(input('Enter a no: '))
#     total = 0
#     for i in range(1,user_input+1,1):
#         total*=i
#         print(i,end=" * ")

#     print("\b\b=",total)
    
# Factorial()


# def Pyramid():

#     for i in range(5):
#         for j in range(5-i-1):
#             print(" ",end="")
#         for j in range(i+1):
#             print("*",end=" ")
#         print()
#     print()

# Pyramid()


# def PYRAMID(x:int,s:any):
#     for i in range(x):
#         for j in range(x-i-1):
#             print(" ",end="")
#         for j in range(i+1):
#             print(s,end=" ")
#         print()
#     print()
# # user_input = int(input('Enter a no.'))
# # symbol = input("Enter a symbol you want to print: ")
# PYRAMID(5,"$")


# def DIMOND(x:int,s:any):
#     for i in range(x):
#         for j in range(x-i-1):
#             print(" ",end="")
#         for j in range(i+1):
#             print(s,end=" ")
#         print()
#     for i in range(x):
#         for j in range(i+1):
#             print(" ",end="")
#         for j in range(x-i-1):
#             print(s,end=" ")
#         print()
#     print()
# user_input = int(input('Enter a no.'))
# symbol = input("Enter a symbol you want to print: ")
# DIMOND(5,"$")


# def DIMOND(x:int,s:any):
#     for i in range(x):
#         for j in range(x-i-1):
#             print(" ",end="")
#         for j in range(i+1):
#             print(s,end=" ")
#         print()
#     for i in range(x):
#         for j in range(i+1):
#             print(" ",end="")
#         for j in range(x-i-1):
#             print(s,end=" ")
#         print()
#     for i in range(x-1):
#         for j in range(x-i-1):
#             print(" ",end="")
#         for j in range(i+1):
#             print(s,end=" ")
#         print()
# # user_input = int(input('Enter a no.'))
# # symbol = input("Enter a symbol you want to print: ")
# DIMOND(5,"$")


# # DAMARU
# def DIMOND(x:int,s:any):
#     for i in range(x+1):
#         for j in range(i+1):
#             print(" ",end="")
#         for j in range(x-i):
#             print(s,end=" ")
#         print()
    
#     for i in range(x):
#         for j in range(x-i):
#             print(" ",end="")
#         for j in range(i+1):
#             print(s,end=" ")
#         print()
# # user_input = int(input('Enter a no.'))
# # symbol = input("Enter a symbol you want to print: ")
# DIMOND(5,"$")