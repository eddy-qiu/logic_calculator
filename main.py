user_input = input("Enter a valid propositional statement: ")
num_variables = int(input("How many variables are there?"))
glb = {}
truth_value = 0

for i in range(num_variables):
    glb["x" + str(i+1)] = 0

for i in range(2 ** num_variables - 1):
    while i > 0:
        if i % 2 == 1:
            glb["x" + str(i+1)] = 1
        else:
            glb["x" + str(i+1)] = 0
        i /= 2
    if eval(user_input, glb):
        truth_value = 1
        break

if truth_value:
    print("The propositional statement is satisfiable")
else:
    print("the propositional statement is unsatisfiable")