# How many ways can four students Ram, Anuj, Deepak and Ravi line up in
# a line, if the order matters?
# Print all the possible Combination.


def all_combination(arr):
    if len(arr) == 0:
        return []

    if len(arr) == 1:
        return [arr]

    comb = []
    for i in range(len(arr)):
        temp = arr[i]
        remaining = arr[:i] + arr[i+1:]
        for a in all_combination(remaining):
            comb.append([temp] + a)
    return comb


students = ["Ram", "Anuj", "Deepak", "Ravi"]
for combination in all_combination(students):
    print(combination)
