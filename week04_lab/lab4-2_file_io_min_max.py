# Problem Lab04-3

import sys

def process_file(fileName):
    input_file = open(fileName, "rt")
    num_list = []

    for line in input_file:
        line = line.rstrip('\n')
        num = int(line)
        num_list.append(num)

    input_file.close()

    min_value = 100000
    max_value = 0

    for number in num_list:
        if number < min_value:
            min_value = number

        if number > max_value:
            max_value = number

    print('min: ', min_value, 'max: ', max_value)

if __name__ == "__main__":
	# process_file(sys.argv[1])
    process_file('list.txt')