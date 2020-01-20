from decorators import cache_decorator

@cache_decorator
def calculator(a, b, operation):
  # Здесь нужно реализовать функцию,
  # которая реализует основные арифметические операции между числами: +, -, /, *, **.
  # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
  operations = ('+', '-', '/', '*','**')

  if any(i == operation for i in operations):
    if (operation == '+'):
      return a + b
    elif (operation == '-'):
      return a - b
    elif (operation == '*'):
      return a * b
    elif (operation == '/'):
      try:
        return a / b
      except ZeroDivisionError:
        return print('делить на ноль нельзя!')
    elif (operation == '**'):
      return a ** b
  else:
    return 'Неверно указан оператор, укажите один из +, -, /, *, **'

if __name__ == '__main__':
  while True:
    try:
      a = int(input('Введите число: ')) 
      break
    except Exception:
      print('Введите целое число')
  while True:
    try:
      b = int(input('Введите число: '))
      break
    except Exception:
      print('Введите целое число')

  operation = input('Введите операцию')

  print('Результат: ', calculator(a, b, operation))

