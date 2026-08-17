# 1 Sum or 5 Values

# a = [10,20,30,40,50] 
# sum=0
# for i in range(5):
#     sum+=a[i]
# print(sum)

# # 2 max

# arr = [10,364,54,5,369]
# max = arr[0]
# for i in range(5):
#     if (arr[i] > max):
#         max = arr[i]
#     print("max = " ,max)

# # 3 min

# arr = [10,364,54,5,369]
# max = arr[0]
# for i in range(5):
#     if (arr[i] < max):
#         max = arr[i]
#     print("max = " ,max)

#4 Count 10 Values of Array By Different Paramete

# arr = [10,-45,0,67,89,78,23,2,0,-1]
# Zero = 0
# Positive = 0
# Negative =0
# Odd = 0
# Even = 0
# for i in range(len(arr)):
#     if(arr[i] < 0):
#         Negative+=1
#     if((arr[i] > 0)):
#         Positive+=1
#     if((arr[i] == 0)):
#         Zero+=1
#     if((arr[i] % 2 !=  0)):
#         Odd+=1
#     else:
#         Even+=1

    
#     print(arr[i])

# print(f"Zero = {Zero} Positive = {Positive} Negative = {Negative} Odd = {Odd} Even = {Even} " )

# 5 Swap a Value from Odd Position to Even Position
# arr = [1,2,3,12,34,54,12,1,2,3]
# temp = arr[0]
# for i in range(0,len(arr) - 1,2):

#     temp = arr[i]
#     arr[i] = arr[i+1]
#     arr[i+1] = temp
# print(arr)

# 6 Acceding Order

# arr = [10,4,7,4,2,1,435,67,9,45]
# temp = arr[0]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if (arr[i] >  arr[j]):
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp

# print ( arr )

    # 7 . Descending  Order

# arr = [10,4,7,4,2,1,435,67,9,45]
# temp = arr[0]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if (arr[i] < arr[j]):
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp

# print ( arr )


# 8. Second Largest No From Given Array (brutal) not woke on [1,2,5,7,7]

# arr = [10,364,574,5,969]
# temp = arr[0]
# for i in range(len(arr)):
#     for j in range (len(arr)):
#         if (arr[i] < arr[j]):
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp

# print("max = " ,arr[len(arr)-2])

# 8. Second Largest No From Given Array

# arr = [10,364,574,5,969]
# largest  = arr[0]
# for i in range(len(arr)):
#     if (arr[i] > largest):
#         largest = arr[i]
    
# second_largest = -1

# for j in range(len(arr)):
#     if (arr[j] > second_largest and arr[j] != largest ):
#         second_largest = arr[j]

# print("Second_Largest", second_largest)
    

# 9 Suppress Zero :- 

# arr = [10,-45,0,67,0,78,23,2,0,-1]
# temp = arr[0]
# for i in range(len(arr)):
#     for j in range (len(arr)):
#         if (arr[j] == 0):
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp

# print("Array = " ,arr)

#  10 Suppress Negative:
# arr = [10,-45,0,67,0,78,23,2,0,-1]
# temp = arr[0]
# for i in range(len(arr)):
#     for j in range (len(arr)):
#         if (arr[j] < 0):
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp

# print("Array = " ,arr)

#  11 Suppress Negative:
# arr = [10,-45,0,67,0,78,23,2,0,-1]
# temp = arr[0]
# for i in range(len(arr)):
#     for j in range (len(arr)):
#         if (arr[j] > 0):
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp

# print("Array = " ,arr)

#  13 Suppress Negative:
# arr = [10,-45,0,67,0,78,23,2,0,-1]
# user_input = int(input('Enter New Value '))
# ind = int(input('Enter a Position of New Value: '))
# arr[ind] = user_input
        
# print("Array = " ,arr)
# 

