
#
# odd_list = []
# for i in range(21):
#     if i % 2 == 1:
#         odd_list.append(i)
#
#
# print(odd_list)



# odd_list = [i for i in range(10) if i % 2 ==1]
#
# print(odd_list)


# 生成器表达式
# odd_list = (i for i in range(21) if i % 2 == 1)
# print(type(odd_list))
#
# for item in odd_list:
#     print(item)



# odd_list = (i for i in range(21) if i % 2 ==1 )
# print(odd_list)
#
# for item in odd_list:
#     print(item)


# 字典推导式
# my_dict = {"tom":22,"tom2":33}
#
# reversed_dict = {value:key for key, value in my_dict.items()}
# print(reversed_dict)

my_dict = {"tom":22,"jack":33}

reversed_dict = {value:key for key, value in my_dict.items()}

print(reversed_dict)






