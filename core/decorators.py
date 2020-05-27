def cache_decorator(f):
  # Реализовать декоратор который кэширует результаты вызова функции (есть в лекции)
  # Применить для функции calculator (в calculator.py уже есть import функции cache_decorator)
  # Настоятельно прошу написать декоратор руками, а не копировать, т.к. важно запомнить как это работает
    
  cache ={}

  def inner(*args):

    if args not in cache:
      cache[args] = f(*args)

    return cache[args]
    
  return inner
