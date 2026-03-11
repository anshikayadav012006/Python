# there are two types of special operator 1. membership operator and 2. identity operator
# membership operator= 1. in 2. not in
# name='Anshika'
# print('Z' in name)
# print('Z' not in name)

# if one not given then it will start from 0 
# for i in range(6):
#     print(i)

# for i in range(1,6):
#     print(i)

# for i in range(1,10,3): # 1 to 10 with difference of 3
#     print(i)


# for i in range(5,0,-1):
#     print(i)


# for i in range(1, 11):
#     print(i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10)


for i in range(1, 11):
    for j in range(2, 11):
        print(i*j, end=" ")
    print()