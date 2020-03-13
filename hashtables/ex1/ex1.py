"""
Missing module docstring
"""

from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,
                        )


def get_indices_of_item_weights(weights, length, limit):
    """
    Return a tuple such that my linter stops raging about
    the missing docstring
    """
    hash_table = HashTable(16)

    for i in range(length):
        hash_table_insert(hash_table, weights[i], i)

    for i in range(length):
        result = hash_table_retrieve(hash_table, limit - weights[i])

        if result:
            return result, i

    return None


def print_answer(answer):
    """
    Error
    """
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
