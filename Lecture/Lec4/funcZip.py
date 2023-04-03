# Функция Zip 

# users = ['user1', 'user2', 'user3', 'user5',]
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) 

# Ответ
# [('user1', 4), ('user2', 5), ('user3', 9), ('user5', 14)]


users = ['user1', 'user2', 'user3', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data) 

# # Ответ
# [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]