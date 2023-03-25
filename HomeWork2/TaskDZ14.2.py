# **** есть девять цыфор от 1 до 9 по возростанию, можем вставить между ними + или - или ничего 
#  найдите все изних которые будут равны 100

### Вариант 1  

def solve_expression(sequence: tuple, expression: str = '') -> None:
    if len(sequence) == 1:
        expression += f'{sequence[0]}'
        if eval(expression) == 100:
            print(f'{expression} == 100')
    else:
        solve_expression(sequence[1:], expression + f'{sequence[0]}')
        solve_expression(sequence[1:], expression + f'{sequence[0]} + ')
        solve_expression(sequence[1:], expression + f'{sequence[0]} - ')


def main():
    sequence_of_digits = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    solve_expression(sequence_of_digits)


if __name__ == '__main__':
    main()

# Ответ :
# 123 + 45 - 67 + 8 - 9 == 100
# 123 + 4 - 5 + 67 - 89 == 100
# 123 - 45 - 67 + 89 == 100
# 123 - 4 - 5 - 6 - 7 + 8 - 9 == 100
# 12 + 3 + 4 + 5 - 6 - 7 + 89 == 100
# 12 + 3 - 4 + 5 + 67 + 8 + 9 == 100
# 12 - 3 - 4 + 5 - 6 + 7 + 89 == 100
# 1 + 23 - 4 + 56 + 7 + 8 + 9 == 100
# 1 + 23 - 4 + 5 + 6 + 78 - 9 == 100
# 1 + 2 + 34 - 5 + 67 - 8 + 9 == 100
# 1 + 2 + 3 - 4 + 5 + 6 + 78 + 9 == 100
