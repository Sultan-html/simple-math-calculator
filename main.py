numbers = list(map(int, input().split()))

total = sum(numbers)
print(total)

max_number = max(numbers)
print(max_number)

average = total / len(numbers)
print(round(average, 2))
