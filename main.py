# Receive input from user
# user_input = a valid propositional statement using x1, x2, x3, etc.
# num_variables = number of xs used (x1, x2 would be 2 vars)
user_input = input("Enter a valid propositional statement: ")
num_variables = int(input("How many variables are there?"))
glb = {}
truth_value = 0

# Put all the variables into the dictionary
for i in range(num_variables):
    glb["x" + str(i + 1)] = 0

# Loop through all the binary representations of all the possible values of the variables
# ie 2^(3 variables-1) will produce 111
for i in range(2 ** num_variables - 1):
    # evaluate first digit
    while i > 0:
        if i % 2 == 1:
            # if the first digit is 1, set the variable to 1 in the dictionary
            glb["x" + str(i + 1)] = 1
        # dividing by two takes away the units digit in binary
        i /= 2

    # bitwise-ly evaluate the user_input given the dictionary values
    # eval is able to calculate propositions because it uses the same notations as bitwise ( | & ~ () )
    if eval(user_input, glb):
        # if the evaluation is true, set truth value to true and break the loop
        truth_value = 1
        break

    # reset the values of everything in the dictionary to 0 after each iteration
    for j in range(num_variables):
        glb["x" + str(j + 1)] = 0

# print the result
if truth_value:
    print("The propositional statement is satisfiable")
else:
    print("the propositional statement is unsatisfiable")