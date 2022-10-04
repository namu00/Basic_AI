# Problem Lab04-3

import sys
def process_file(fileName):
    input_file = open(fileName, "r")

    result_list = []

    for idx, line in enumerate(input_file):
        line = line.rstrip('\n')

        if idx == 0:
            content_str = line + ',합계,평균'
            result_list.append(content_str)
            continue
        else:
            # print(line)
            name, kor, eng, math = line.split(',')
            # print(name, kor, eng, math)
            tot_sum = float(kor) + float(eng) + float(math)
            tot_avg = tot_sum / 3
            content_str = line + ',' + str(tot_sum) + ',' + str(tot_avg)
            # print(content_str)
            result_list.append(content_str)
    input_file.close()

    print(result_list)

    # file write

    output_file = open('output.csv', "wt")
    
    for line in result_list:
        output_file.write(line + '\n')
    
    output_file.close()

if __name__ == "__main__":
    # process_file(sys.argv[1])
    process_file('input.csv')
