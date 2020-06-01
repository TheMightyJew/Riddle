import copy


def get_all_permutations(length):
    permutations = []
    for i in range(1,6):
        permutation = [i]
        add_number(permutations, length-1, permutation)
    return permutations


def add_number(permutations, length, permutation):
    if length == 0:
        permutations.append(permutation)
        a = 1
        return
    if permutation[-1] != 5:
        newPermutation = copy.deepcopy(permutation)
        newPermutation.append(newPermutation[-1]+1)
        add_number(permutations, length - 1, newPermutation)
    if permutation[-1] != 1:
        newPermutation = copy.deepcopy(permutation)
        newPermutation.append(newPermutation[-1]-1)
        add_number(permutations, length - 1, newPermutation)


def get_all_shot(length):
    solutions = []
    for i in range(1, 6):
        solution = [i]
        add_sol(solutions, length - 1, solution)
    return solutions


def add_sol(solutions, length, solution):
    if length == 0:
        solutions.append(solution)
        a = 1
        return
    for i in range(1, 6):
        newSolution = copy.deepcopy(solution)
        newSolution.append(i)
        add_sol(solutions, length - 1, newSolution)


def get_valid_solutions(length):
    solutions = get_all_shot(length)
    permutations = get_all_permutations(length)
    valid_solutions = []
    for solution in solutions:
        valid = True
        for second_permutation in permutations:
            worked = False
            for i in range(len(solution)):
                if solution[i] == second_permutation[i]:
                    worked = True
                    break
            if not worked:
                valid = False
                break
        if valid:
            valid_solutions.append(solution)
    return valid_solutions


length = 1
while True:
    solutions = get_valid_solutions(length)
    if len(solutions) != 0:
        print('Solution with minimal length of', length, 'found:')
        print(solutions)
        break
    else:
        length += 1
