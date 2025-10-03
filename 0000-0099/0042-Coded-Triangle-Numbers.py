def word_value(word: str) -> int:
	return sum(ord(c) - ord('A') + 1 for c in word)


def triangle_numbers(limit: int) -> set[int]:
	triangles = set()
	n = 1
	t = 0
	while t <= limit:
		t = n * (n + 1) // 2
		triangles.add(t)
		n += 1

	return triangles


def solution():
	words = eval(open('0042_words.txt').read())
	max_word_val = max(word_value(w) for w in words)
	triangles = triangle_numbers(max_word_val)
	result = sum(1 for w in words if word_value(w) in triangles)
	return result


result = solution()
print(result)
