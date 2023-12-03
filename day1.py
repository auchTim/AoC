Values = ['1abc2','pqr3stu8vwx','a1b2c3d4e5f','treb7uchet']
output = 0
for word in Values:
    numbers = []
    last = 0
    first = 0
    for char in word:
        if char.isdigit():
            numbers.append(char)
    #print(numbers)
    last = numbers[len(numbers) - 1]
    first = numbers[0]
    concat = str(first) + str(last)
    number = int(concat)
    output = output + number 
print(f"the secret number is: {output}")