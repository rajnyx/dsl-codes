# hash table using linear probing
# size = 10
# hash_table = []

# for i in range(size):
#     hash_table.append("EMPTY")

# def insert(key):
#     idx = key % size
#     if key not in hash_table:
#         for i in range(size):
#             probe_idx = (idx + i) % size
#             if hash_table[probe_idx] == "EMPTY" or hash_table[probe_idx] == "DELETED":
#                 hash_table[probe_idx] = key
#                 print(f"Key {key} inserted.")
#                 return
#     else:
#         print(f"Key {key} already exists.")

# def search(key):
#     idx = key % size
#     for i in range(size):
#         probe_idx = (idx + i) % size
#         if hash_table[probe_idx] == key:
#             print(f"Key {key} found.")
#             return
#     print(f"Key {key} not found.")

# def delete(key):
#     idx = key % size
#     for i in range(size):
#         probe_idx = (idx + i) % size
#         if hash_table[probe_idx] == key:
#             hash_table[probe_idx] = "DELETED"
#             print(f"Key {key} deleted.")
#             return
#     print(f"Key {key} not found.")

# def display():
#     print("Hash Table:")
#     for i in range(size):
#         print(f"Index {i}: {hash_table[i]}")

# A Tree is a non-linear data structure used to store data in a hierarchical manner.

    #       50
    #      /  \
    #     30   70
    #    / \   / \
    #   20 40 60 80

# 1. Root: The topmost node of the tree.
# Here, 50 is the root.

# 2. Node: Every individual element in a tree is called a node.
# Here, 50, 30, 70, 20, 40, 60 and 80 are nodes.

# 3. Parent: A node that has children.
# For example, 50 is the parent of 30 and 70.

# 4. Child: A node directly connected below another node.
# 30 and 70 are children of 50.

# 5. Leaf Node: A node that has no children.
# Here, 20, 40, 60 and 80 are leaf nodes.

# 6. Edge: The connection between two nodes.
# For example, the connection between 50 and 30 is an edge.

# 7. Subtree: A smaller tree inside a bigger tree.
# For example, the tree starting at 30 is a subtree.

# A Binary Tree is a tree in which each node can have at most two children.
# A Binary Search Tree is a special type of Binary Tree that follows a particular rule.

# The rule is:
# 1. All smaller values go to the LEFT.
# 2. All greater values go to the RIGHT.
# 3. The same rule applies to every node in the tree.
# 50, 30, 70, 20, 40, 60, 80
# root = 50
# left_child = 30
# right_child = 70
# left_child_left = 20
# left_child_right = 40
# right_child_left = 60
# right_child_right = 80
# 50 becomes the root.
# 30 is smaller than 50, so it goes left.
# 70 is greater than 50, so it goes right.
# 20 is smaller than 50 AND smaller than 30, so it goes left of 30.
# 40 is smaller than 50 but greater than 30, so it goes right of 30.
# 60 is greater than 50 but smaller than 70, so it goes left of 70.
# 80 is greater than both 50 and 70, so it goes right of 70.


def create_node(data):
    return {"data" : data,
            "left" : None,
            "right" : None
    } 

def insert(root, data):
    if root is None:
        create_node(data)

    elif root["data"] < data:
        root["right"] = insert(root["right"], data)
    elif root["data"] > data:
        root["left"] = insert(root["left"], data)

    return root

def search(root, key):
    if root is None:
        return False
    if root["data"] < key:
        return search(root["right"], key)
    elif root["data"] > key:
        return search(root["left"], key)
    else:
        return True

def display(root):
    if root:
        display(root["left"])
        print(root["data"], end=" ")
        display(root["right"])

def find_min(root):
    while root["left"]:
        root = root["left"]
    return root

def delete(root, key):
    if root is None:
        return None

    if root["data"] < key:
        root["right"] = delete(root["right"], key)
    elif root["data"] > key:
        root["left"] = delete(root["left"], key)

    if root["left"] is None:
        return root["right"]
    elif root["right"] is None:
        return root["left"]

    temp = find_min(root["right"])
    root["data"] = temp["data"]
    root["right"] = delete(root["right"], temp["data"])

    return root

    