# 1. Sum or 5 Values
# dict_arr = {}
# sum = 0
# for i in range(5):
#     a = int(input('Enter element: '))
#     dict_arr[i] = a
#     sum += dict_arr[i]
    
# print(sum)
    

# 2. Max Value 
# dict_arr = {0: 10, 1: 620, 2: 230, 3: 440, 4: 50}
# max = -1
# for values in dict_arr.values():
#     if (max < values):
#         max = values
    
# print(max)

#4  Count 10 Values of Array By Different Paramete

# dict_arr = {0: 10,1: -45,2: 0,3: 67,4: 89,5: 78,6: 23,7: 2,8: 0,9: -1}
# Zero = 0
# Positive = 0
# Negative = 0
# Odd = 0
# Even = 0
# for value in dict_arr.values():
#     print(value)
#     if ( value  == 0):
#         Zero+=1
#     elif value < 0 :
#         Negative+=1
#     elif value > 0 :
#         Positive+=1
    
#     if(value % 2 == 0):
#         Even +=1 
#     else:
#         Odd+=1
# print(f"Zero = {Zero} Positive = {Positive} Negative = {Negative} Odd = {Odd} Even = {Even} " )


# 5. Swap a Value from Odd Position to Even Position
# dict_no = {1:102,2:2,3:12,4:34,5:43,6:78}
# # temp = dict_no[1]
# # print(temp)
# for i in range (1,len(dict_no)):
#     dict_no[i],dict_no[i+1] = dict_no[i+1],dict_no[i]
#     # temp = dict_no[i]
#     # dict_no[i] = dict_no[i+1]
#     # dict_no[i+1] = temp
    
# print(dict_no)

# 6 Acceding Order
# dict_no = {1:102,2:2,3:12,4:34,5:43,6:78}
# temp = dict_no[1]
# for i in range(1,len(dict_no)+1):
#     for j in range(1,len(dict_no)+1):
#         if (dict_no[i] >  dict_no[j]):
#             temp = dict_no[i]
#             dict_no[i] = dict_no[j]
#             dict_no[j] = temp

# print(dict_no)
