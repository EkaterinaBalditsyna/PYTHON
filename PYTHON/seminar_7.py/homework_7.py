# def f(words):
#     return sum(1 for i in words if i in 'аеёиоуыэюя')
    
    
# c = "Хорошо-живет-на-свете-Винни-Пух! Оттого-поет-он-эти-Песни-вслух!"
# st = c.lower().split()
# t = f(st[0])
# if all([f(i) == t for i in st]):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')


def print_operation_table(operation, num_rows=9, num_columns=9):
    for i in range(1, num_rows + 1):
        answer = []
        for j in range(1, num_columns + 1):
            answer.append(str(operation(i, j)))
        print("     ".join(answer))
  
print_operation_table(lambda x, y: x * y)