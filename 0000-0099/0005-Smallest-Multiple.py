import math
from functools import reduce

def solution():
	lcm = lambda a, b: a * b // math.gcd(a, b)
	return reduce(lcm, range(1, 21))

result = solution()
print(result)
