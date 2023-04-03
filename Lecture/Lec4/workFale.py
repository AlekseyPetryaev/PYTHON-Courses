# Работа с файлами 

# colors = ['red', 'green', 'blue', '8888'] 
# data = open('file.txt', 'a')  # здесь указываем режим, в котором будет работать 
# data.writelines(colors) # разделителей не будет 
# data.close()

# Ответ
# Создается фаил(file.txt) и вкладывается в него (redgreenblue8888)


# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# print(56)

# Ответ
# Создается фаил(file.txt) и вкладывается в него (
# line 1
# line 2)


path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()