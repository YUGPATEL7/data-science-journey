
# 1 Count String Length
# string = "My Name is Yug Patel"
# print(len(string))

# 2 Word Count
# string = "My Name is Yug Patel"
# count = 1
# for s  in string:
#     if s == " ":
#         count+=1
# print(count) 

#  3 Vovel Count (A, E, I , O, U)
# string = "My Name is Yug Patel"
# Vovel_Count = 0
# for s in string:
#     if s == "A" or s == "a" or s == "E" or s == "e" or s == "I" or s == "i" or s == "O" or s == "o" or s == "U" or s == "u"  :
#         Vovel_Count +=1
# print(Vovel_Count)


#4  Find Char
# string = "My Name is Yug Patel"
# user_char = input("Enter a  char : ")
# count = 0
# for s in string : 
#     if s == user_char:
#         count +=1 
# print(count)

#5 Replace Char
# string = "My Name is Yug Patel"
# first_char = input("Enter Replace Char: ")
# second_char = input("Enter New  Char: ")

# new_string = list(string)
# for i in range(len(new_string)):
#     if new_string[i] == first_char:
#         new_string[i] = second_char
# string = "".join(new_string)    
# print(string)


#6 Reverse String 
# string = "My Name is Yug Patel"
# lenght = len(string)
# new_string = list(string)
# reversed_list = []
# for i in range(lenght,0,-1):
#     reversed_list.append(new_string[i-1])

# string = "".join(reversed_list)
# print(string)

# 7 Penindrom String

# string = "nayan"
# lenght = len(string)
# new_string = list(string)
# reversed_list = []
# reversed_string = ""
# for i in range(lenght,0,-1):
#     reversed_list.append(new_string[i-1])

# reversed_string = "".join(reversed_list)
# if(reversed_string == string):
#     print("This is Penindrom  String")
# else:
#     print("This is not a  Penindrom  String")
    

# 8 Encrepted String


# 10 Upper case 
# A = 65 , Z= 90 & a = 97 , z= 122
# m = 109 - > M =  77 
# y = 121 -> y = 89
# string = "my name is yug patel"

# new_string = list(string)
# new_list = []
# for s in new_string:
#     o = ord(s)
#     if o == 32:
#         new_list.append(" ")
#     else:
#         a= o - 32
#         a= chr(a)
#         new_list.append(a) 

# string = "".join(new_list)
# print(string)

# 11 lower case 
# string = "MY NAME IS YUG "

# new_string = list(string)
# new_list = []
# for s in new_string:
#     o = ord(s)
#     if o == 32:
#         new_list.append(" ")
#     else:
#         a= o + 32
#         a= chr(a)
#         new_list.append(a) 

# # 12 Toggle case 
# string = "My Name IS YUG "

# new_string = list(string)
# new_list = []
# for s in new_string:
#     o = ord(s)
#     if o == 32:
#         new_list.append(" ")
#     elif o > 90 :
#         a= o - 32
#         a= chr(a)
#         new_list.append(a) 
#     else:
#         a= o + 32
#         a= chr(a)
#         new_list.append(a) 

# string = "".join(new_list)
# print(string)

# 13 Toggle case 
# string = "My Name Is Yug "

# new_string = list(string)
# Suppers = ""
# new_list = []
# for s in new_string:
#     o = ord(s)
#     if o == 32:
#         new_list.append(" ")
#     elif o > 90 :
#         # a= o - 32
#         # a= chr(a)
#         Suppers += s
#         # new_list.append(a) 
#     else:

#         new_list.append(s) 

# string = "".join(new_list)
# string = string + Suppers
# print(string)


#  15 Insert Charater
# string = "My Name is Yug Patel"
# first_char = input("Please Enter New Char ")
# pos = int(input("Enter Posstion : "))
# list_string = list(string)
# for i in range(len(string)):
#     if i == pos:
#         list_string[i] = first_char
# string = "".join(list_string)    
# print(string)

# 16 Delete Charater
# string = "My Name is Yug Patel"
# first_char = input("Please Enter New Char ")

# list_string = list(string)
# for s in string:
#     if s == first_char:
#         print("o")
#     else:
#         list_string.append(s)

# string2 = "".join(list_string)    
# print(string2)

# 17 Left & right Trim 

# string = "    Java"
# new_string = []

# for s in string:
#     if s == " ":
#         pass
#     else:
#         new_string.append(s)
# trmied = "".join(new_string)    
# print(trmied)


# 21 Find Word 

# string = "My name is Yug"
# word = input("Please Enter Find Word: ")

# if word in string:
#     print("yes")
# else:
#     print("No")

# 22 Write a Program For Count Char as How Many Time Char Available in String? 

# string = "hello world"
# dict_string = dict()
# a=0     
# for s in string:
#     dict_string[s] = 0
#     a+=1


# for s in string:
#     if(s in dict_string):
#         dict_string[s] +=1

# print("Char Count: ")
# for key , values in dict_string.items():
#     print(key,"\t",values)






# Extar 

# string = "I am writing c code"
# new_list =[]
# new_string = ""
# new_list=string.split(" ")
# reversed_list = []
# s_word = ""
# temp = ""
# for s in new_list:
#     for i in range(len(s)-1,-1,-1):

#             s_word+=s[i]
#     reversed_list.append("")
#     reversed_list.append(s_word)
#     s_word=""

# string = " ".join(reversed_list)
# print(string)

# 
string = "photosynthesis"
new_list = list(string)
a = 0
b=''
s=''
pause = ""
for i in range(len(string)):   # i = 2
    if( pause == "stop"):
        break
    for j in range(i) : # j = 2 
        if(a < len(string)):
            b= ord(new_list[a]) - 32
            s=chr(b)
            if(j == 0):
                print(s,end="")
                a+=1
            else:
                print(new_list[a],end="")
                a+=1
        else:
            pause = "stop"
            print("*",end='')
    print()



