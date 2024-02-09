def generate_permutations(string, start, end):
    if start == end:
        print(''.join(string))
    else:
        for i in range(start, end + 1):
            # Swap characters
            string[start], string[i] = string[i], string[start]
            # Recur with the next position
            generate_permutations(string, start + 1, end)
            # Undo the swap for backtracking
            string[start], string[i] = string[i], string[start]

def print_permutations():
    user_input = input("Enter a string: ")
    string = list(user_input)
    generate_permutations(string, 0, len(string) - 1)

print_permutations()
