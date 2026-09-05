# Binary Search Tree

A complete implementation of a Binary Search Tree (BST) in Python with full support for standard tree operations.

## Description

This project provides a robust implementation of a Binary Search Tree data structure, featuring:

- **BSTNode**: Represents individual tree nodes with key, value, and parent pointers
- **BinarySearchTree**: Main class with essential BST operations

## Features

- **Insert**: Add key-value pairs while maintaining BST ordering
- **Search**: Find nodes by key efficiently
- **Delete**: Remove nodes handling three cases (leaf, one child, two children)
- **Traversals**: In-order, pre-order, and post-order traversals
- **Magic Methods**: Support for `len()`, `in`, iteration, and string representation
- **Helper Methods**: `_successor()` and `_predecessor()` for advanced operations

## Usage

```python
from BinaryTree import BinarySearchTree

# Create a BST
bst = BinarySearchTree()

# Insert key-value pairs
bst.insert(10, "Ismail")
bst.insert(5, "hamada")
bst.insert(22, "sam")
bst.insert(2, "salah")

# Search for a node
node = bst.search(10)

# Check if key exists
if 10 in bst:
    print("Key found!")

# Delete a node
bst.delete(5)

# Traverse the tree
for key, value in bst.traverse("inorder"):
    print(f"{key}: {value}")

# Iterate through the tree
for key, value in bst:
    print(f"{key}: {value}")
```

## Time Complexity

- Insert: O(log n) average, O(n) worst case
- Search: O(log n) average, O(n) worst case
- Delete: O(log n) average, O(n) worst case

## Installation

Clone the repository and run:

```bash
python BinaryTree.py
```

## Project Structure

```text
📂 BinarySearchTree/
├── 📄 BinaryTree.py
├── 📄 README.md
```

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## Author

Ismail - [@Imismail18](https://github.com/Imismail18)

## License

MIT License

Copyright (c) 2026 Ismail

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

