# # library book borrowing records

# dict1 = {
#     "MEM1": ["Book A", "Book B", "Book C"],
#     "MEM2": ["Book A", "Book C"],
#     "MEM3": ["Book B"],
#     "MEM4": []
# }

# # 1. Average number of books borrowed

# counts = []

# for books in dict1.values():
#     counts.append(len(books))

# print("Average books borrowed:", sum(counts) / len(counts))

# # this will show the frequency of each book borrowed
# freq_books = {}
# for li in dict1.values():
#     for book in li:
#         freq_books[book] = freq_books.get(book, 0) + 1

# # print the book that was borrowed the most
# max_book = max(freq_books, key=freq_books.get)
# print("Most borrowed book:", max_book)
# # print the book that was borrowed the least
# min_book = min(freq_books, key=freq_books.get)
# print("Least borrowed book:", min_book)

# 3. Members who borrowed no books
# print("Members who borrowed no books:")
# for member in dict1:
#     if len(dict1[member]) == 0:
#         print(member)

# 5. Time and space complexity
# print("Time Complexity: O(n*m)")
# print("Space Complexity: O(n*m)")

# search using linear and binary search
# def linear_search(arr, key):
#     for i in range(len(arr)):
#         if arr[i] == key:
#             print("ID found using Linear Search")
#             return
#     print("ID not found using Linear Search")


# def binary_search(arr, key):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == key:
#             print("ID found using Binary Search")
#             return
#         elif arr[mid] < key:
#             low = mid + 1
#         else:
#             high = mid - 1

#     print("ID not found using Binary Search")


# arr = [10, 20, 30, 40, 50]

# key = int(input("Enter customer ID: "))

# linear_search(arr, key)
# binary_search(arr, key)

# selection sort
# arr = [64,25,12,22,11]
# for i in range(len(arr)):
#     min_idx = i

#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[min_idx]:
#             min_idx = j

#     arr[i], arr[min_idx] = arr[min_idx], arr[i]

# bubble sort
# arr = [64, 34, 25, 12, 22, 11]
# for i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# text editor using stack
# class TextEditor:
#     def __init__(self):
#         self.document = ""
#         self.undo_stack = []
#         self.redo_stack = []

#     def write(self, text):
#         self.undo_stack.append(self.document)
#         self.document += text
#         self.redo_stack.clear()

#     def undo(self):
#         if self.undo_stack:
#             self.redo_stack.append(self.document)
#             self.document = self.undo_stack.pop()
#         else:
#             print("Nothing to undo.")

#     def redo(self):
#         if self.redo_stack:
#             self.undo_stack.append(self.document)
#             self.document = self.redo_stack.pop()
#         else:
#             print("Nothing to redo.")

#     def display(self):
#         print("Current Document:", self.document)

# editor = TextEditor()
# editor.write("Hello ")

# real time event processing using queue
# event_queue = []
# def add_event(event):
#     event_queue.append(event)
#     print(f"Event '{event}' added to the queue.")

# def process_event():
#     if event_queue:
#         event = event_queue.pop(0)
#         print(f"Processing event: {event}")
#     else:
#         print("No events to process.")

# def display_events():
#     if event_queue:
#         print("Current events in the queue:")
#         for event in event_queue:
#             print(event)
#     else:
#         print("No events in the queue.")

# def cancel_event(event):
#     if event in event_queue:
#         event_queue.remove(event)
#         print(f"Event '{event}' canceled.")
#     else:
#         print(f"Event '{event}' not found in the queue.")

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