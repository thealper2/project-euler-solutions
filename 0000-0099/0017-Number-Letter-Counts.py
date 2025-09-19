def number_to_words(n):
    ones = ["","one","two","three","four","five","six","seven","eight","nine",
            "ten","eleven","twelve","thirteen","fourteen","fifteen",
            "sixteen","seventeen","eighteen","nineteen"]
    tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

    if n == 1000:
        return "onethousand"
    elif n >= 100:
        hundreds = ones[n // 100] + "hundred"
        if n % 100 != 0:
            return hundreds + "and" + number_to_words(n % 100)
        return hundreds
    elif n >= 20:
        return tens[n // 10] + ones[n % 10]
    else:
        return ones[n]

def solution():
	return sum(len(number_to_words(i)) for i in range(1, 1001))

result = solution()
print(result)
