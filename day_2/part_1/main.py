with open('input.txt', 'r') as input_file:
    opcode = input_file.read()
    opcode_list = opcode.split(',')  # Splits the input file into a list

    for i in range(0, len(opcode_list)):
        opcode_list[i] = int(opcode_list[i]) # Converts the list from strings to integers

    opcode_list[1] = 12
    opcode_list[2] = 2

    for opcode_location in range(0, len(opcode_list), 4):
        opcode = opcode_list[opcode_location]
        if opcode == 1:
            sum_location = opcode_list[opcode_location + 3]
            opcode_list[sum_location] = opcode_list[opcode_list[opcode_location + 1]] + opcode_list[opcode_list[opcode_location + 2]]
        elif opcode == 2:
            sum_location = opcode_list[opcode_location + 3]
            opcode_list[sum_location] = opcode_list[opcode_list[opcode_location + 1]] * opcode_list[opcode_list[opcode_location + 2]]
        elif opcode == 99:
            break
        else:
            break

    print(opcode_list[0])
