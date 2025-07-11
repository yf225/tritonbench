from tritonbench.operators import list_operators


def get_operators():
    """
    Retrieve the list of operators for the default collection.

    This function retrieves the list of operators for the default collection by
    comparing the operators from the 'all' collection and the 'liger' collection.
    It returns a list of operators that are present in the 'all' collection but
    not in the 'liger' collection.

    In the future, if we add more operator collections, we will need to update
    this function to exclude desired operators in other collections.

    other_collections = list_operator_collections()
    to_remove = set(other_collections).union(liger_operators)
    return [item for item in all_operators if item not in to_remove]

    Returns:
        List[str]: A list of operator names for the default collection.
    """
    return list_operators()
