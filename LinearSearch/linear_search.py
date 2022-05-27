import random

def linear_search(search_element, element_list):
    '''
    Linear search function to return the list index if the element is found.
    Otherwise return -1
    '''
    for index in range(len(element_list)):  # or can use range(0, len(element_list), 1)
        if element_list[index] == search_element:
            return index
    else:
        # If element is not found or the list is empty, return -1
        return -1


# Generate a list with 10 random element between 1 to 50
element_list = random.sample(range(1, 50), 10)

print("Element List", element_list)

# Select a random number which we want to search in the element
search_element = random.randint(0, 50)

# call the linear search function to search the element
result = linear_search(search_element, element_list)

if result != -1:
    print(f"Element {search_element} found at index {result}")
else:
    print(f"Element {search_element} not found!")


# If we want search a char in string

word = "Hello World!"
search = "W"

print("\nWord is", word)

# call the linear search function to search the element
result = linear_search(search, word)

if result != -1:
    print(f"Element {search} found at index {result}")
else:
    print(f"Element {search} not found!")