import getopt, sys
import traceback


def create_output(unique_list):

    output_order = ['PERSON', 'PLACE', 'ANIMAL', 'COMPUTER', 'OTHER']
    legal_categories = {'PERSON':0, 'PLACE':0, 'ANIMAL':0, 'COMPUTER':0, 'OTHER':0}

    # Iterating the index
    for i in range(len(unique_list)):
        category = unique_list[i].split(' ')[0]

        if category in legal_categories:
            legal_categories[category] += 1

    print('CATEGORY' + ' ' + 'COUNT')
    for i in range(len(output_order)):
        print(output_order[i] + ' ' + str(legal_categories[output_order[i]]))

    for i in range(len(unique_list)):
        category = unique_list[i].split(' ')[0]
        if category in legal_categories:
            print(unique_list[i])


def get_input():

    # Get full command-line arguments
    full_cmd_arguments = sys.argv

    # Keep all but the first
    argument_list = full_cmd_arguments[1:]
    fileName = argument_list[0]

    f = open(fileName, "r")
    input = f.read()

    return input.split('\n')


def main():

    try:
        #get input
        unique_list = []
        lines = get_input()

        for line in lines:
            if line.rstrip() not in unique_list:
                unique_list.append(line.rstrip())

        create_output(unique_list)
    except:
        print("Error while generating output")
        traceback.print_exc()


if __name__ == '__main__':
    main()












