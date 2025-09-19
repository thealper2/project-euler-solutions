def is_prime(n):
	for a in range(2, int(n**0.5)):
		if n % a == 0:
			return False
	
	return True

def solution(x=600851475143):
	max_prime = float('-inf')
	for i in range(2, int(x**0.5)):
		if x % i == 0:
			if is_prime(i):
				max_prime = max(max_prime, i)
			elif is_prime(x // i):
				max_prime = max(max_prime, x // i)

	return max_prime

result = solution()
print(result)
