import random
# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def gen(N):

    for i in range(N):
     
      yield random.randint(0, 100)

# написать генераторное выражение, которое делает то же самое
gen2 = (random.randint(0, 100) for i in range(10))
