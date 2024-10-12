from bloom_filter import BloomFilter
from constants.config import MAX_ELEMENTS, ERROR_PROBABILITY, MAX_ELEMENT_LENGTH
from constants.operations import BREAK, ADD, CHECK

def main():
    bloom = BloomFilter(MAX_ELEMENTS, ERROR_PROBABILITY)

    file_name = 'input.txt'
    output = []

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if line == BREAK:
                break
            operation, item = line[0], line[1:].strip()
            if len(item) <= MAX_ELEMENT_LENGTH and item.isalpha():
                if operation == ADD:
                    bloom.add(item)
                elif operation == CHECK:
                    result = bloom.check(item)
                    output.append(result)

    for result in output:
        print(result)


if __name__ == "__main__":
    main()
