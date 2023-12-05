def import_values(path):
    input_file = open(path, 'r')
    return input_file

def main():
    Values = import_values('./1/problem_values')
    output = 0
    mapping = {'one': 1 , 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    mapping_keys = list(mapping.keys())

    for word in Values:
        numbers = []

        for key in mapping_keys:
            if key in word:  
                kindex = word.index(key)
                numbers.append([kindex, mapping[key]])

        for index, char in enumerate(word):
            if char.isdigit():
                numbers.append([index , int(char)])

        print(numbers)
        # still using the whole subarray instead of only the first value to find min
        # find a way to get the second value via accessing the first -> dictionaries? 2D array?
        lowest =  min([min(sublist) for sublist in numbers])
        highest = max([max(sublist) for sublist in numbers])
        print(lowest, highest)

        #fix the adding of numbers to get the end result

        #first = numbers[0]
        #concat = str(first) + str(last)
        #number = int(concat)
        #output = output + number
    print(f"the secret number is: {output}")

main()