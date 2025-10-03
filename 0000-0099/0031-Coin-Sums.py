def solution():
	target = 200
	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	ways = [0] * (target + 1)
	ways[0] = 1

	for c in coins:
		for amt in range(c, target + 1):
			ways[amt] += ways[amt - c]

	return ways[target]

result = solution()
print(result)
