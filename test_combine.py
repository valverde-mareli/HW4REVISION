from combine import combine_lists

# Test 1: example from prompt
print(combine_lists([3, 1, 5], [2, 5, 4]))
# Expected: [5, 4, 3, 2, 1]

# Test 2: duplicates
print(combine_lists([1, 2, 2], [3, 4, 4]))
# Expected: [4, 3, 2, 1]

# Test 3: empty lists
print(combine_lists([], []))
# Expected: []

# Test 4: one empty, one non-empty
print(combine_lists([7, 3, 7], []))
# Expected: [7, 3]

# Test 5: negative numbers
print(combine_lists([-1, 5, 3], [0, -1]))
# Expected: [5, 3, 0, -1]

# Test 6: TypeError check
try:
    combine_lists([1, 2, "3"], [4])
except TypeError:
    print("TypeError raised correctly")
