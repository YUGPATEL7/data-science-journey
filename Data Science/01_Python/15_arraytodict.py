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

# 7. Descending Order
# dict_no = {1:102,2:2,3:12,4:34,5:43,6:78}
# temp = dict_no[1]
# for i in range(1,len(dict_no)+1):
#     for j in range(1,len(dict_no)+1):
#         if (dict_no[i] <  dict_no[j]):
#             temp = dict_no[i]
#             dict_no[i] = dict_no[j]
#             dict_no[j] = temp

# print(dict_no)

# 8. Second Largest No From Given Array
# dict_no = {1:10,2:4,3:7,4:2,5:1,6:435,7:9,8:45}
# largest = dict_no[1]

# for i in range(1,len(dict_no)+1):
#     if (dict_no[i] > largest):
#         largest = dict_no[i]

# second_largest= -1
# for j in range(1,len(dict_no)+1):
#     if (dict_no[j] > second_largest and dict_no[j] != largest):
#         second_largest = dict_no[j]

# print(second_largest)


# 8. Suppress Zero
# dict_no = {1:10,2:4,3:0,4:0,5:1,6:435,7:9,8:0}
# temp = 0

# for j in range (1,len(dict_no)):
#     for i in range(1,len(dict_no)):
#         if (dict_no[i] == 0 ):
#             temp = dict_no[i]
#             dict_no[i] = dict_no[i+1]
#             dict_no[i+1]= temp

# print(dict_no)

# 8. Suppress Negative
# dict_no = {1:10,2:-4,3:0,4:0,5:1,6:-435,7:-9,8:0}
# temp = 0

# for j in range (1,len(dict_no)):
#     for i in range(1,len(dict_no)):
#         if (dict_no[i] < 0 ):
#             temp = dict_no[i]
#             dict_no[i] = dict_no[i+1]
#             dict_no[i+1]= temp

# print(dict_no)

# 8. Suppress Postive
# dict_no = {1:-10,2:-4,3:0,4:0,5:1,6:-435,7:9,8:0}
# temp = 0

# for j in range (1,len(dict_no)):
#     for i in range(1,len(dict_no)):
#         if (dict_no[i] > 0 ):
#             temp = dict_no[i]
#             dict_no[i] = dict_no[i+1]
#             dict_no[i+1]= temp

# print(dict_no)


# 12. Insert Value at Given Position

# dict_no = {1:10,2:20,3:30,4:40,5:50}
# value =int(input('Enter a value :'))
# pos =int(input('Enter a Position of New Value: '))

# for i in range(1,len(dict_no)+1):
#     if(i == pos):
#         dict_no[i] = value

# print(dict_no)


# 13. Delete a Duplicate Values

# dict_no = {1:10,2:20,3:30,4:10,5:20}
# unique_values = list(set(dict_no.values()))
# new_dict = dict()
# for i in range(len(unique_values)):
#     new_dict[i] = unique_values[i]
# print(new_dict)


# 14. Delete Given Values
# dict_no = {1:10,2:20,3:30,4:10,5:20}
# user_input = int(input('Enter a value that you have to delete: '))

# for i in range(1,len(dict_no)+1):
#     if (dict_no[i] == user_input):
#         dict_no.pop(i)
# print(dict_no)

