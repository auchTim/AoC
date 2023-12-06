def import_values(path):
    input_file = open(path, 'r')
    return input_file

def main():
    Values = import_values('./1/input')
    output = 0
    mapping = {'one': 1 , 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    mapping_keys = list(mapping.keys())

    for word in Values:
        numbers = {}

        for key in mapping_keys:
            if key in word:
                kindex = word.index(key)
                numbers.update({kindex : mapping[key]})

        for index, char in enumerate(word):
            if char.isdigit():
                #print(index, char)
                numbers.update({index : int(char)})
        print("Index : Value")
        print(numbers)

        lowest = numbers[min(numbers.keys())]
        highest = numbers[max(numbers.keys())]
        print("erster Wert und letzter Wert")
        print(lowest, highest)

        concat = str(lowest) + str(highest)
        output = int(concat) + output
    print(f"the secret number is: {output}")

main()