# Python Data Types: A Comprehensive Guide

This repository contains a detailed overview of Python data types. Python, being a dynamically typed language, allows variables to change type during the execution of the program. Understanding Python's built-in data types is crucial for every Python developer, whether you're just starting or looking to deepen your knowledge.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Text Data Types](#text-data-types)
   - [str](#str)
3. [Numeric Data Types](#numeric-data-types)
   - [int](#int)
   - [float](#float)
   - [complex](#complex)
4. [Sequence Data Types](#sequence-data-types)
   - [list](#list)
   - [tuple](#tuple)
   - [range](#range)
5. [Mapping Data Type](#mapping-data-type)
   - [dict](#dict)
6. [Set Data Types](#set-data-types)
   - [set](#set)
   - [frozenset](#frozenset)
7. [Boolean Data Type](#boolean-data-type)
   - [bool](#bool)
8. [Binary Data Types](#binary-data-types)
   - [bytes](#bytes)
   - [bytearray](#bytearray)
   - [memoryview](#memoryview)
9. [None Data Type](#none-data-type)
   - [NoneType](#nonetype)
10. [Conclusion](#conclusion)

---

## Introduction

In Python, **data types** represent the kind of data stored in a variable. Every value in Python has a data type, and the language automatically determines the type of data when a value is assigned to a variable.

Understanding Python's data types is fundamental for writing efficient code. This guide will cover the most common data types used in Python and their usage.

---

## Text Data Types

### `str` (String)
A string in Python is a sequence of characters enclosed in single, double, or triple quotes (`'`, `"`, or `'''`/`"""`).

#### Example:
```python
text = "Hello, World!"
print(type(text))  # <class 'str'>
