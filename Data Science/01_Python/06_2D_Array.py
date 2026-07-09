#  Bacis fo 2D Array 

# a = [[0 for _ in range(2)] for _ in range (5)]  [[col] row]
# print(a)

# 1  2d Values All Sum

# arr = [[0 for _ in range(2)] for _ in range (2)]
# print(len(arr))
# sum = 0 
# for i in range(len(arr)):
#     for j in range (len(arr)):
#         arr[i][j] = int(input('Enter a No. '))
#         sum+=arr[i][j]
        
# print(arr)
# print(sum)

# 2  2d Array Min / Max Value

# arr = [[10,4,5],[0,2,0]]
# min = -1
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if(arr[i][j] < min ):
#             min = arr[i][j]

# print(f"min = {min}")


# 3 Possitve, Nagative, Odd, Even, Zero Count 
# Zero = 0
# Positive = 0
# Negative = 0
# Odd = 0
# Even = 0
# for i in range(len(arr)):
#     for j in range (len(arr[i])):
#         if(arr[i][j] ==  0):
#             Zero+=1
#         elif(arr[i][j] < 0 ):
#             Negative+=1
#         elif(arr[i][j] > 0 ):
#             Positive+=1

#         if(arr[i][j] % 2 == 0):
#             Even+=1
#         else:
#             Odd+=1
# print(f"Zero = {Zero} Positive = {Positive} Negative = {Negative} Odd = {Odd} Even = {Even} " )


# 4 Row Wise Ascending 

# arr =  [[10,4,5],
#         [0,2,0],
#         [48,2,3]]
# temp = arr[0][0]
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#                 if (arr[i][j] < arr[i][k]):
#                         temp = arr[i][j]
#                         arr[i][j] = arr[i][k]
#                         arr[i][k] = temp
# print(f"Array = {arr}")

# 5 Full Ascending 


# arr =  [[10,4,5],
#         [0,2,0],
#         [48,2,3]]
# temp = arr[0][0]
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#                 for l in range(3):
#                         if (arr[i][j] < arr[k][l]):
#                                 temp = arr[i][j]
#                                 arr[i][j] = arr[k][l]
#                                 arr[k][l] = temp
# print(f"Array = {arr}")

# 6. Transpose Matrix:

# arr = [
#     [10, 1, 234],
#     [2, 24, 3],
#     [12, 5, 2]
# ]

# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         temp = arr[i][j]
#         arr[i][j] = arr[j][i]
#         arr[j][i] = temp

# print("Transpose Matrix:")
# for row in arr:
#     print(row)


# 6. Symetrix Matrix:

# arr = [
#     [10, 1, 234],
#     [2, 24, 3],
#     [12, 5, 2]
# ]

# print("Symetrix Matrix:")
# for row in arr:
#     print(row)