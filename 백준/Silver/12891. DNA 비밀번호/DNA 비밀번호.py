import sys
input = sys.stdin.readline

def check_conditions(counter, required):
    for c in "ACGT":
        if counter[c] < required[c]:
            return False
    return True

def solve_dna(s, length, required):
    counter = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in range(length):
        counter[s[i]] += 1

    valid_count = 1 if check_conditions(counter, required) else 0

    for i in range(length, len(s)):
        counter[s[i]] += 1
        counter[s[i - length]] -= 1
        if check_conditions(counter, required):
            valid_count += 1

    return valid_count



n,m = map(int,input().split())
dna = list(map(str,input().strip()))
required_counts = list(map(int, input().split()))
required = {'A': required_counts[0], 'C': required_counts[1], 'G': required_counts[2], 'T': required_counts[3]}


result = solve_dna(dna, m, required)
print(result)
