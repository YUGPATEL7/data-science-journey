# 2D dict 
# taking an input form user 
# toD_dict = dict()
# sum =0
# for i in range(3):
#     toD_dict[i] = dict() 
#     print("Your are on ", i)
#     for j in range (3):
#         user_input = int(input(f"Enter your element for {j} :"))
        
#         toD_dict[i][j] = user_input
# print(toD_dict) 

# 1 sum
# toD_dict = {0: {0: 45, 1: 6, 2: 4}, 1: {0: 1, 1: 4, 2: 7}, 2: {0: 9, 1: 5, 2: 3}}
# sum =0
# for i in range(3):
#     for j in range (3):
#         sum+=toD_dict[i][j] 
# print(sum) 


# 2 min
# toD_dict = {0: {0: 45, 1: 6, 2: 4}, 1: {0: 1, 1: 4, 2: -7}, 2: {0: 9, 1: 5, 2: 3}}
# min = toD_dict[0][0]
# for i in range(3):
#     for j in range (3):
#         if (min > toD_dict[i][j]  ):
#             min= toD_dict[i][j] 
# print(min) 

# 3 max
# toD_dict = {0: {0: 45, 1: 6, 2: 4}, 1: {0: 1, 1: 4, 2: -7}, 2: {0: 9, 1: 55, 2: 3}}
# max = toD_dict[0][0]
# for i in range(3):
#     for j in range (3):
#         if (max< toD_dict[i][j]):
#             max = toD_dict[i][j] 
# print(max) 

# # 4. Row Wise Ascending
# toD_dict = {0: {0: 45, 1: 6, 2: 4}, 1: {0: 1, 1: 4, 2: -7}, 2: {0: 9, 1: 55, 2: 3}}
# temp = toD_dict[0][0]
# for i in range(3):
#     for j in range (3):
#         for k in range (3):
#             if (toD_dict[i][j] < toD_dict[i][k]):
#                 temp = toD_dict[i][j]
#                 toD_dict[i][j] = toD_dict[i][k]
#                 toD_dict[i][k] = temp
# print(toD_dict) 

# # 5. Full Ascending
# toD_dict = {0: {0: 45, 1: 6, 2: 4}, 1: {0: 1, 1: 4, 2: -7}, 2: {0: 9, 1: 55, 2: 3}}
# temp = toD_dict[0][0]
# for i in range(3):
#     for j in range (3):
#         for k in range (3):
#             for l in range(3):
#                 if (toD_dict[i][j] < toD_dict[k][l]):
#                     temp = toD_dict[i][j]
#                     toD_dict[i][j] = toD_dict[k][l]
#                     toD_dict[k][l] = temp
# print(toD_dict) 

# 6. Transpose Matrix:

# toD_dict = {0: {0: 45, 1: 6, 2: 4}, 1: {0: 1, 1: 4, 2: -7}, 2: {0: 9, 1: 55, 2: 3}}
# temp = 0
# for i in range(3):
#     for j in range (i+1,3):
#             temp = toD_dict[i][j]
#             toD_dict[i][j] = toD_dict[j][i]
#             toD_dict[j][i] =temp
# print(toD_dict) 


# 8 sum 