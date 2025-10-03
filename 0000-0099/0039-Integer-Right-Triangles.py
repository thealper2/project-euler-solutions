from collections import defaultdict


def solution():
	limit = 1000
	cnt = defaultdict(int)

	for a in range(1, limit // 2):
		for b in range(a, (limit - a) // 2 + 1):
			c = (a ** 2 + b ** 2) ** 0.5
			if c.is_integer():
				p = a + b + int(c)
				if p <= limit:
					cnt[p] += 1

	best_p, _ = max(cnt.items(), key=lambda x: x[1])
	return best_p


result = solution()
print(result)
