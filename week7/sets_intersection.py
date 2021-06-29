from functools import reduce

print(reduce(lambda current, x: str(current) + ' ' + str(x),
             sorted(set(map(int, input().split())).
                    intersection(set(map(int, input().split()))))))
