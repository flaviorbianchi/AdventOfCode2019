# read input into list
with open('day2.1-input.txt') as f:
    intcode = f.readlines()

# convert input into a list of integer values
intcode = list(map(int, intcode[0].split(",")))

# Once you have a working computer, the first step is to restore 
# the gravity assist program (your puzzle input) to the "1202 program alarm" 
# state it had just before the last computer caught fire. To do this, before 
# running the program, replace position 1 with the value 12 and replace 
# position 2 with the value 2.
intcode[1] = 12
intcode[2] = 2

index = 0

# Iterate until position index arrives at opcode 99, halting the program.
while intcode[index] != 99:
    leftvalue = intcode[intcode[index+1]]
    rightvalue = intcode[intcode[index+2]]

    if (intcode[index] == 1):
        result = leftvalue + rightvalue
    else:
        result = leftvalue * rightvalue

    intcode[intcode[index+3]] = result

    index += 4

# What value is left at position 0 after the program halts?
print(intcode[0])