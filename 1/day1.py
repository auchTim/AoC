def import_values(path):
    input_file = open(path, 'r')
    return input_file

def main():
    Values = import_values('./1/input_test')
    output = 0
    mapping = {'one': 1 , 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    mapping_keys = list(mapping.keys())
    for word in Values:
        numbers = []
        last = 0
        first = 0
        for key in mapping_keys:
            if key in word:
                word = word.replace(key,str(mapping[key]))
        print(word)
        for char in word:
            if char.isdigit():
                numbers.append(char)
        print(numbers)
        #print(numbers)
        last = numbers[len(numbers) - 1]
        first = numbers[0]
        concat = str(first) + str(last)
        number = int(concat)
        output = output + number
    print(f"the secret number is: {output}")

main()