# Write a Python program to manage the borrowing records of books in a library. Implement the following functionalities:
# • Compute the average number of books borrowed by all library members.
# • Find the book with the highest and lowest number of borrowings in the library.
# • Count the number of members who have not borrowed any books (denoted by a borrow count of 0).
# • Display the most frequently borrowed book (i.e., the mode of borrow counts).
# After performing, determine the time and Space complexity of each operation
# dict1 = {
#     "MEM1": ["Book A", "Book B", "Book C"],
#     "MEM2": ["Book A", "Book C"],
#     "MEM3": ["Book B"],
#     "MEM4": []
# }

# # 1. Average number of books borrowed
# total = 0

# for book in dict1.values():
#     total += len(book)

# members = len(dict1)
# print("Average books borrowed:", total / members)

# # Time Complexity: O(n)
# # Space Complexity: O(1)


# # 2. Frequency of each book
# freq_books = {}

# for book in dict1.values():
#     for b in book:
#         freq_books[b] = freq_books.get(b, 0) + 1

# print("Frequency of each book:", freq_books)

# # Time Complexity: O(n + b) average
# # Space Complexity: O(u)


# # 3. Highest and lowest borrowed books
# max_book = max(freq_books, key=freq_books.get)
# min_book = min(freq_books, key=freq_books.get)

# print("Most borrowed book:", max_book)
# print("Least borrowed book:", min_book)

# # Time Complexity: O(u)
# # Space Complexity: O(1)

# # 4. Members who borrowed zero books
# count = 0

# for member in dict1:
#     if len(dict1[member]) == 0:
#         count += 1
#         print("Member with zero borrowing:", member)

# print("Total members with zero borrowing:", count)

# # Time Complexity: O(n)
# # Space Complexity: O(1)

# # 5. Mode of borrowing counts
# "How many members have borrowed the same number of books, and which borrowing count occurs most frequently?"
# borrow_counts = []
# for member in dict1:
#     borrow_counts.append(len(dict1[member]))
# mode = {}
# for c in borrow_counts:
#     mode[c] = mode.get(c,0) + 1
# print("max mode : ", max(mode,key=mode.get))
# Time Complexity: O(n)
# Space Complexity: O(n)

# In an e-commerce system, customer account IDs are stored in a list, and you are tasked with writing a program that implements
# the following:
# • Linear Search: Check if a particular customer account ID exists in the list.
# • Binary Search: Implement Binary search to find if a customer account ID exists, improving the search efficiency over the basic
# linear.
# ids = [101, 102, 103, 104, 105]
# n = int(input("enter the id you want to search for : "))
# for i in ids:
#     if i == n:
#         print("ID found using Linear Search")
#         break
# print("ID not found using Linear Search")

# def binary_search(arr,key):
#     arr.sort()
#     low = 0
#     high = len(arr) - 1
#     while (low <= high):
#         mid = (low + high) / 2
#         if(arr[mid] == key):
#             print("ID found using Binary Search")
#             return
#         elif(arr[mid]<key):
#             low = mid + 1
#         else:
#             high = mid - 1
#     print("ID not found using Binary Search")
# binary_search(arr, key)


# Problem statement: In a company, employee salaries are stored in a list as floating-point numbers. Write a python program that
# sorts the employee salaries in ascending order using following two algorithms:
# 1. Selection sort: Sort the values using the selection sort algorithm
# 2. Bubble sort: Sort the salaries using bubble sort algorithm
# After sorting the salaries, the program should display top 5 highest salaries in the company.
# selection sort
# arr = [64, 34, 25, 12, 22, 11]
# for i in range(len(arr)):
#     min_idx = i
#     for j in range(i+1, len(arr)):
#         if (arr[j]<arr[min_idx]):
#             min_idx = j
#     arr[i], arr[min_idx] = arr[min_idx], arr[i]
# print(arr)

# bubble sort
# arr = [64, 34, 25, 12, 22, 11]

# for i in range(len(arr)-1):
#     for j in range(0, len(arr)-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)

# Implementing a real-time undo/redo system for a text editing application using a Stack data structure. The system should support
# the following operations:
# - Make a Change: A new change to the document is made.
# - Undo Action: Revert the most recent change and store it for potential redo.
# - Redo Action: Reapply the most recently undone action.
# - Display Document State: Show the current state of the document after undoing or redoing an action
# text editor using stack
# document = ""
# undo_stack = []
# redo_stack = []

# def write(text):
#     undo_stack.append(document)
#     document += text
#     redo_stack.clear()

# def undo():
#     # Python allows you to read a global variable 
#     # inside a function, but if you want to MODIFY or reassign it, you need global.
#     global document
#     if undo_stack:
#         redo_stack.append(document)
#         document = undo_stack.pop()
#     else:
#         print("Nothing to undo.")

# def redo():
#     global document
#     if redo_stack:
#         undo_stack.append(document)
#         document = redo_stack.pop()
#     else:
#         print("Nothing to redo.")

# def display():
#     global document
#     print("Current Document:", document)

# Implement a real-time event processing system using a Queue data structure.
# The system should support the following features:
# - Add an Event: When a new event occurs, it should be added to the event queue.
# - Process the Next Event: The system should process and remove the event that has been in the queue the longest.
# - Display Pending Events: Show all the events currently waiting to be processed.
# - Cancel an Event: An event can be canceled if it has not been processed
# real time event processing using queue
# event_queue = []

# # Add event
# def add_event(event):
#     event_queue.append(event)
#     print("Event added")

# # Process event
# def process_event():
#     if event_queue:
#         event_queue.pop(0)
#         print("Event processed")
#     else:
#         print("No events to process")

# # Display events
# def display_events():
#     print("Current events:")
#     for event in event_queue:
#         print(event)

# # Cancel event
# def cancel_event(event):
#     if event in event_queue:
#         event_queue.remove(event)
#         print("Event cancelled")
#     else:
#         print("Event not found")


# # Main program
# add_event("Meeting")
# add_event("Workshop")
# add_event("Seminar")

# display_events()

# process_event()

# display_events()

# cancel_event("Seminar")

# display_events()

# enqueue --> add an element to the end of the queue (append)
# dequeue --> remove an element from the front of the queue (pop(0))

# hash table using chaining
# size = 10
# hash_table = [[] for _ in range(size)]

# def insert(key):
#     idx = key % size
#     if key not in hash_table[idx]:
#         hash_table[idx].append(key)
#         print(f"Key {key} inserted.")
#     else:
#         print(f"Key {key} already exists.")

# def search(key):
#     idx = key % size
#     if key in hash_table[idx]:
#         print(f"Key {key} found.")
#     else:
#         print(f"Key {key} not found.")

# def delete(key):
#     idx = key % size
#     if key in hash_table[idx]:
#         hash_table[idx].remove(key)
#         print(f"Key {key} deleted.")
#     else:
#         print(f"Key {key} not found.")

# def display():
#     print("Hash Table:")
#     for i in range(size):
#         print(f"Index {i}: {hash_table[i]}")

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

# Implement various operations on a Binary Search Tree, such as insertion, deletion, display, and search.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# # Insert a node
# def insert(root, data):
#     if root is None:
#         return Node(data)

#     if data < root.data:
#         root.left = insert(root.left, data)
#     else:
#         root.right = insert(root.right, data)

#     return root


# # Search a node
# def search(root, key):
#     if root is None:
#         return False

#     if root.data == key:
#         return True
#     elif key < root.data:
#         return search(root.left, key)
#     else:
#         return search(root.right, key)


# # Display BST (Inorder)
# def display(root):
#     if root:
#         display(root.left)
#         print(root.data, end=" ")
#         display(root.right)


# # Find minimum value
# def find_min(root):
#     while root.left:
#         root = root.left
#     return root


# # Delete a node
# def delete(root, key):
#     if root is None:
#         return None

#     if key < root.data:
#         root.left = delete(root.left, key)

#     elif key > root.data:
#         root.right = delete(root.right, key)

#     else:
#         if root.left is None:
#             return root.right

#         elif root.right is None:
#             return root.left

#         temp = find_min(root.right)
#         root.data = temp.data
#         root.right = delete(root.right, temp.data)

#     return root


# # Main program
# root = None

# while True:
#     print("\n\n1. Insert")
#     print("2. Search")
#     print("3. Delete")
#     print("4. Display")
#     print("5. Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         value = int(input("Enter value: "))
#         root = insert(root, value)

#     elif choice == 2:
#         value = int(input("Enter value to search: "))
#         if search(root, value):
#             print("Value found")
#         else:
#             print("Value not found")

#     elif choice == 3:
#         value = int(input("Enter value to delete: "))
#         root = delete(root, value)

#     elif choice == 4:
#         print("BST in sorted order:")
#         display(root)

#     elif choice == 5:
#         break

#     else:
#         print("Invalid choice")