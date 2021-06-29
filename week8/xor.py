from functools import reduce

print(reduce(lambda current, x: str(current) + ' ' + str(x),
             map(lambda x: x[0] ^ x[1],
                 zip(
                     map(int, input().split()),
                     map(int, input().split())
                 ))))
