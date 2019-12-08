with open('input.txt', 'r') as input_file:
    opcode = input_file.read()
    opcode_list = opcode.split(',')  # Splits the input file into a list

    for i in range(0, len(opcode_list)):
        opcode_list[i] = int(opcode_list[i]) # Converts the list from strings to integers


    for noun in range(0, 99):
        for verb in range(0, 99):
            list_copy = opcode_list.copy()

            list_copy[1] = noun
            list_copy[2] = verb

            for opcode_location in range(0, len(list_copy), 4):
                opcode = list_copy[opcode_location]
                if opcode == 1:
                    sum_location = list_copy[opcode_location + 3]
                    list_copy[sum_location] = list_copy[list_copy[opcode_location + 1]] + list_copy[list_copy[opcode_location + 2]]
                elif opcode == 2:
                    sum_location = list_copy[opcode_location + 3]
                    list_copy[sum_location] = list_copy[list_copy[opcode_location + 1]] * list_copy[list_copy[opcode_location + 2]]
                elif opcode == 99:
                    break
                else:
                    break
            if list_copy[0] == 19690720:
                answer = 100 * noun + verb
                print(answer)
                quit()
