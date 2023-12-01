# sum of calibration values
sum = 0

with open('./input.txt') as file:
    for line in file: 
        numbers = []
        for c in line:
            if c.isdigit():
                numbers.append(c)
        if len(numbers) == 1:
            sum += int(numbers[0] + numbers[0])
        elif len(numbers) > 1:
            sum += int(numbers[0] + numbers[-1])

print(sum)

