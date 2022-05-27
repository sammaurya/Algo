import random

def linear_search_index_range(search_element, element_list, start, end):
    '''
    Linear search function to return the list index if the element is found in the given
    index range. Otherwise return -1
    '''
    for index in range(start, end+1):
        if element_list[index] == search_element:
            return index
    else:
        # If element is not found or the list is empty, return -1
        return -1


# Generate a list with 10 random element between 1 to 50
element_list = random.sample(range(1, 50), 10)

print("Element List", element_list)

# Select a random number which we want to search in the element
random_index = random.randint(0, 10)
search_element = element_list[random_index]

# call the linear search function to search the element
result = linear_search_index_range(search_element, element_list, 1, 6)

if result != -1:
    print(f"Element {search_element} found at index {result}")
else:
    print(f"Element {search_element} not found!")


# If we want search a char in string

word = "Hello World!"
search = "W"

print("Word is", word)

# call the linear search function to search the element
result = linear_search_index_range(search, word, 1, 7)

if result != -1:
    print(f"Element {search} found at index {result}")
else:
    print(f"Element {search} not found!")