user_input = input("Enter a valid propositional statement: ")
num_variables = int(input("How many variables are there?"))
truth_value = 0

for x1 in range(0, 2):
    for x2 in range(0, 2):
        for x3 in range(0, 2):
            for x4 in range(0, 2):
                if eval(user_input):
                    truth_value = 1
                    break

if truth_value:
    print("The propositional statement is satisfiable")
else:
    print("the propositional statement is unsatisfiable")
