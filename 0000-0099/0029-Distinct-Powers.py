seen = set()
for a in range(2, 101):
	for b in range(2, 101):
		if a**b not in seen:
			seen.add(a**b)

print(len(seen))
