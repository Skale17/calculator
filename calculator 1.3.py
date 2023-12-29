def plus(x, y):
    return x+y

def minus(x, y):
    return x-y

def multiplication(x, y):
    return x*y

def division(x, y):
    if y==0:
        print('нельзя делить на ноль')
    else:
        return x/y

def degree(x, y):
    return x**y

def root(x,y):
    return x**(1/y)
operators = {
            '+':plus,
            '-':minus,
            '/':division,
            '*':multiplication,
            '**':degree,
            'корень':root,
        }
while True:
    try:
        try_example = input('все через пробел максимум два значения есть 7 вариаций операций +, -, /, *, **, корень и то какой корень')
        example = try_example.split()
        str_number1, operation, *str_number2 = example 
    except:
        print('неверные данные')
        continue
    try:
        fl_number_1 = float(str_number1)
        fl_number_2 = float(*str_number2)
    except:
        print('введенны неверные числа') 
        continue
    
    if operation in operators:
        result = operators[operation](fl_number_1, fl_number_2)
        result_finish = round(result, 2)
        print(result_finish)
    else:
        print('неверный оператор')
    



    repeat = input('продолжаем да/нет')
    if repeat.lower() != 'да':
        break

