# My alg:
#  1) create a dictionary with children as the keys and parents as the values
#  2) build up 'paths' to ancestors with a dft, and keep track of all paths
#  3) return the ancestor at the tip of the longest 'path'
        # 3.1) or the ancestor with the lowest id in a tie-breaker
        # 3.2) or, if the starting node has no parents, -1

from util import Stack

def earliest_ancestor(ancestors, starting_node):
    longest_path = [starting_node]

    to_visit = Stack()
    to_visit.push([starting_node])

    visited = set()

    parents_dict = get_parents_dict(ancestors)

    while to_visit.size() > 0:
        current_path = to_visit.pop()
        last_node = current_path[-1]

        if len(current_path) > len(longest_path) or (len(current_path) == len(longest_path) and last_node < longest_path[-1]):
            longest_path = current_path

        if last_node not in visited:
            visited.add(last_node)

            if last_node in parents_dict:
                for child_node in parents_dict[last_node]:
                    to_visit.push(current_path + [child_node])

    return longest_path[-1] if len(longest_path) > 1 else -1


def get_parents_dict(ancestors):
    parents_dict = {}

    for parent_child_tuple in ancestors:
        parent = parent_child_tuple[0]
        child = parent_child_tuple[1]

        if child in parents_dict:
            parents_dict[child] = parents_dict[child] + [parent]
        else:
            parents_dict[child] = [parent]

    return parents_dict

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(get_parents_dict(test_ancestors))
# print(earliest_ancestor(test_ancestors, 6))
# print(earliest_ancestor(test_ancestors, 10))