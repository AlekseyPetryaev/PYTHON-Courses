"""
Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за 
всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись 
исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. 
Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках 
располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50
Input:    6 -> -20 30 -40 50 10 -10
Output: 2
"""
from task_random import randint


analyzed_period = int(input('Укажите анализируемый период, дней:\n>>> '))
observation_history = [randint(-50, 50) for _ in range(analyzed_period)]
longest_thaw = 0
current_length = 0
for day in observation_history:
    if 0 < day:
        current_length += 1
        if longest_thaw < current_length:
            longest_thaw = current_length
    else:
        current_length = 0
pretty_text = "\t;\n".join([f"{x[0]}\t|\t{x[1]}" for x in enumerate(observation_history, 1)])
print('Анализируемый период, день | температура:\n'
      f'{pretty_text}\t.\n'
      f'Самая длительная оттепель, дней -> {longest_thaw}')