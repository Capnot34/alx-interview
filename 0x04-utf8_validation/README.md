# UTF-8 Validation

## Introduction
This project focuses on validating whether a given dataset represents a valid UTF-8 encoding using Python. You will apply your knowledge in bitwise operations, understanding of the UTF-8 encoding scheme, and Python programming skills to accomplish this task.

## Concepts Needed
To successfully complete this project, it is required to be familiar with the following concepts:
- Bitwise Operations in Python
- UTF-8 Encoding Scheme
- Data Representation
- List Manipulation in Python
- Boolean Logic

## Tasks
### 0. UTF-8 Validation
Write a method `validUTF8(data)` that determines if a given dataset represents a valid UTF-8 encoding.

- Prototype: `def validUTF8(data)`
- Return: `True` if data is a valid UTF-8 encoding, else return `False`
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers, where each integer represents 1 byte of data
- Therefore, you only need to handle the 8 least significant bits of each integer
