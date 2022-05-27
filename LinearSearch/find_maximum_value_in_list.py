import random

def max_val_in_list(element_list):
    '''
    Function return the Maximum value in the list if the list is not empty.
    Otherwise return None
    '''
    if element_list:
        found_at_index = 0
        ans = element_list[found_at_index]
    else:
        found_at_index = -1
        ans = None
    
    for index in range(len(element_list)):
        if element_list[index] > ans:
            ans = element_list[index]
            found_at_index = index
    
    # If want only the min value not the index
    # for val in element_list:
    #     if val < ans:
    #         ans = val
    
    return ans, found_at_index


# Generate a list with 10 random element between 1 to 50
element_list = random.sample(range(1, 50), 10)

print("Element List", element_list)

# call the linear search function to search the element
result, index = max_val_in_list(element_list)

if result:
    print(f"Maximum element in the list {element_list} is {result} found at index {index}")
else:
    print(f"List is empty")

# If the list is empty
element_list = []
print("\nElement List", element_list)

# call the linear search function to search the element
result, index = max_val_in_list(element_list)

if result:
    print(f"Maximum element in the list {element_list} is {result} found at index {index}")
else:
    print(f"List is empty")


# If we min char in the given string of chars

word = "HelloWorld"

print("\nWord is", word)

# call the linear search function to search the element
result, index = max_val_in_list(word)

if result:
    print(f"Maximum char in the string {word} is {result} found at index {index}")
else:
    print(f"String is empty")