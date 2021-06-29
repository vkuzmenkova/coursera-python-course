from functools import reduce

print(reduce(lambda x, current: current * x, map(lambda x: x ** 5, map(int,
                                                  input().split()))))
