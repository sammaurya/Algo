import random

def max_val_in_2d_list(element_list):
    '''
    Function return the maximum value in the 2d list if the list is not empty.
    Otherwise return None
    '''
    if element_list and element_list[0]:
        row, col = 0, 0
        found_at_index = [row, col]
        ans = element_list[row][col]
    else:
        found_at_index = [-1, -1]
        ans = None
    
    for r in range(len(element_list)):
        for c in range(len(element_list[r])):
            if element_list[r][c] > ans:
                ans = element_list[r][c]
                found_at_index = [r, c]
    
    # If we want only min value not the index
    # for rows in element_list:
    #     for val in rows:
    #         if val > ans:
    #             ans = val

    return ans, found_at_index

def print_2d_list(element_list):
    print()
    for r in range(len(element_list)):
        print(f"    {element_list[r]}")
    print()

# Generate a 2d list with random element between 1 to 50
element_list = [random.sample(range(1, 50), 4) for i in range(random.randint(1, 5))]

print("Element List:")
print_2d_list(element_list)

# call the linear search function to search the element
result, index = max_val_in_2d_list(element_list)

if result:
    print(f"Maximum element in the 2d list is {result} found at index {index}")
else:
    print(f"List is empty")

# If the list is empty
element_list = [[]]
print("\nElement List:")
print_2d_list(element_list)

# call the linear search function to search the element
result, index = max_val_in_2d_list(element_list)

if result:
    print(f"Maximum element in the 2d list is {result} found at index {index}")
else:
    print(f"List is empty")


# If we min char in the given string of chars

word = ["HelloWorld",
        "GoodMorning"
        ]

print("\nElement List:")
print_2d_list(word)

# call the linear search function to search the element
result, index = max_val_in_2d_list(word)

if result:
    print(f"Maximum char in the 2d string is {result} found at index {index}")
else:
    print(f"String is empty")