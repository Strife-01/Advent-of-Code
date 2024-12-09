import re
import sys
import copy


def solve_for_wire(wire, instructions):
    # parse the instructions
    remaining_commands = instructions
    # the wires
    wires = {}
    # as long as we have commands with non integer values
    while len(remaining_commands) != 0:
        # index of current command
        i = 0
        # length of the remaining_commands
        length = len(remaining_commands)
        while i < length:
            # retrieve the current command
            command = remaining_commands[i]
            # getting the inputs and outputs
            input, output = command.split(' -> ')
            # if we give direct input to a wire
            # also check if after separation we have an input in a list
            check = input.split(' ')
            if len(check) == 1:
                if input.isnumeric():
                    # populate the wires dictionary with the direct value
                    wires[output] = int(input)
                    # remove the command from the remaining_commands
                    remaining_commands.remove(command)
                    # correct the remaining length
                    length -= 1
                    continue
                else:
                    # if the wire gets an input from a direct non numeric input we check if we can take it from our values from wires
                    if input in wires:
                        # if the input is already in the wires we redirect the input
                        wires[output] = wires[input]
                        # remove the command from the remaining_commands
                        remaining_commands.remove(command)
                        # correct the remaining length
                        length -= 1
                        continue
                    # in case we still don't have an input for this operation we skip it for now
                    else:
                        # move to the next command
                        i += 1
                        continue

            # in case we have a command we separate the inputs from the actual command
            input_comp = input.split(' ')
            # if the command is NOT
            if len(input_comp) == 2:
                # in case the input is a number
                if input_comp[1].isnumeric():
                    # populate the wires table with the inverse of this wire
                    wires[output] = 65535 - int(input_comp[1])
                    # remove the command from the remaining_commands
                    remaining_commands.remove(command)
                    # correct the remaining length
                    length -= 1
                    continue
                # if it is not numeric we check to see if it exists in the wires table or if we need to parse it again    
                else:
                    # if we already have this input in wires
                    if input_comp[1] in wires:
                        # populate the wires table with the inverse of this wire
                        wires[output] = 65535 - wires[input_comp[1]]
                        # remove the current command
                        remaining_commands.remove(command)
                        # correcting the length
                        length -= 1
                        continue
                    else:
                        # move to the next command
                        i += 1
                        continue
                
            # the last case is with length of 3 which is the 2 inputs and the command
            # safeguard for input of len 3
            if len(input_comp) == 3:
                in_1, com, in_2 = input_comp
                # if the inputs are both direct we compute the value and add it into the wires table
                if in_1.isnumeric() and in_2.isnumeric():
                    # check for commands:
                    if com == 'AND':
                        wires[output] = int(in_1) & int(in_2)
                    elif com == 'OR':
                        wires[output] = int(in_1) | int(in_2)
                    elif com == 'LSHIFT':
                        wires[output] = int(in_1) << int(in_2)
                    else:
                        # the last one is RSHIFT
                        wires[output] = int(in_1) >> int(int_2)
                    # remove the command from the remaining commands
                    remaining_commands.remove(command)
                    # correct the length
                    length -= 1
                    continue
                else:
                    # take the possibility of one of them being an int
                    if in_1.isnumeric() or in_2.isnumeric():
                        # if the first one in numeric:
                        if in_1.isnumeric():
                            # check to see if the 2nd one has a numeric value in the wires table
                            # check if the 2nd input is in wires
                            if in_2 in wires:
                                # means we have numeric value
                                # check for commands:
                                if com == 'AND':
                                    wires[output] = int(in_1) & wires[in_2]
                                elif com == 'OR':
                                    wires[output] = int(in_1) | wires[in_2]
                                elif com == 'LSHIFT':
                                    wires[output] = int(in_1) << wires[in_2]
                                else:
                                    # the last one is RSHIFT
                                    wires[output] = int(in_1) >> wires[int_2]
                                # remove the command from the remaining commands
                                remaining_commands.remove(command)
                                # correct the length
                                length -= 1
                                continue
                            # in case it isn't we move on with the next command
                            else:
                                i += 1
                                continue
                        # if the 2nd input is numeric same operation but in reverse
                        else:
                            # check to see if the 1st one has a numeric value in the wires table
                            # check if the 1st input is in wires
                            if in_1 in wires:
                                # means we have numeric value
                                # check for commands:
                                if com == 'AND':
                                    wires[output] = wires[in_1] & int(in_2)
                                elif com == 'OR':
                                    wires[output] = wires[in_1] | int(in_2)
                                elif com == 'LSHIFT':
                                    wires[output] = wires[in_1] << int(in_2)
                                else:
                                    # the last one is RSHIFT
                                    wires[output] = wires[in_1] >> int(in_2)
                                # remove the command from the remaining commands
                                remaining_commands.remove(command)
                                # correct the length
                                length -= 1
                                continue
                            # in case it isn't we move on with the next command
                            else:
                                i += 1
                                continue
                    # if none of them are numeric we check if we have any of them in the wires else we move on and we do everything again
                    else:
                        # in case both have numeric values inside wires
                        if in_1 in wires and in_2 in wires:
                            # check for commands:
                            if com == 'AND':
                                wires[output] = wires[in_1] & wires[in_2]
                            elif com == 'OR':
                                wires[output] = wires[in_1] | wires[in_2]
                            elif com == 'LSHIFT':
                                wires[output] = wires[in_1] << wires[in_2]
                            else:
                                # the last one is RSHIFT
                                wires[output] = wires[in_1] >> wires[int_2]
                            # remove the command from the remaining commands
                            remaining_commands.remove(command)
                            # correct the length
                            length -= 1
                            continue
                        # else we move on to the next command as if it is not in wires we have nothing to compare
                        else:
                            i += 1
                            continue
            # safeguard
            i += 1

    return wires[wire]



with open(sys.argv[1]) as file:
    instructions = []
    for line in file:
        instructions.append(line.strip())
    copy_instructions = copy.deepcopy(instructions)

result = solve_for_wire(sys.argv[2], copy_instructions)


# override wire b with the solution and solve again
for instruction in instructions:
    if 'b' in instruction.split(' '):
        print(instruction)
