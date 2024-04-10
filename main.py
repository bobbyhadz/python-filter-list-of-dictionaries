# How to filter a List of Dictionaries in Python

list_of_dictionaries = [
    {'id': 1, 'name': 'alice'},
    {'id': 2, 'name': 'bobby'},
    {'id': 3, 'name': 'carl'},
]

list_of_values = [1, 3]

filtered_list_of_dicts = [
    dictionary for dictionary in list_of_dictionaries
    if dictionary['id'] in list_of_values
]

# 👇️ [{'id': 1, 'name': 'alice'}, {'id': 3, 'name': 'carl'}]
print(filtered_list_of_dicts)