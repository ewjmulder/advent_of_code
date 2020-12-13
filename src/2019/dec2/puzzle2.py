input = open("input1", "r")
lines = input.readlines()

program = [int(n) for n in lines[0].split(",")]
initial_program = program.copy()

for noun in range(1, 100):
    for verb in range(1, 100):
        try:
            program = initial_program.copy()
            program[1] = noun
            program[2] = verb

            i = 0
            while i < len(program):
                action = program[i]
                if action == 99:
                    break
                elif action == 1 or action == 2:
                    n1 = program[program[i + 1]]
                    n2 = program[program[i + 2]]
                    if action == 1:
                        # print("add:", n1, n2, program[i + 3])
                        program[program[i + 3]] = n1 + n2
                    if action == 2:
                        # print("mul:", n1, n2, program[i + 3])
                        program[program[i + 3]] = n1 * n2
                # print(program)
                i += 4

            if program[0] == 19690720:
                print(100 * noun + verb)
        except:
            pass
