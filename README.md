
Assignment 3: Understanding Algorithm Efficiency and Scalability

Overview

This repository contains the implementations and performance evaluation of two fundamental algorithms:

1. Randomized Quicksort
2. Hash Table with Chaining

The purpose is to analyze efficiency, scalability, and practical behavior under different data conditions.

Files in This Repository

- `Implementation.py`: Runs benchmarking of Randomized vs. Deterministic Quicksort
- `randomized_quicksort.py`: Contains the implementation of Randomized Quicksort
- `deterministic_quicksort.py`: Contains the implementation of Deterministic Quicksort (pivot = first element)
- `hashing.py`: Implementation of a Hash Table using Chaining
- `Assignment3_Algorithmic_Efficiency_Report.docx`: Detailed report with analysis, results, and discussion
- `README.md`: This file


How to Run the Code

Prerequisites
- Python 3.10 or higher installed on your system

Steps

1. Clone or download the repository to your local machine.
2. Open a terminal in the project directory.
3. Run the benchmark script:

```bash
python Implementation.py
```

This will output runtime results for both sorting algorithms under various input cases:
- Random arrays
- Already sorted arrays
- Reverse-sorted arrays
- Arrays with repeated elements


Summary of Findings

- Randomized Quicksort has a consistent performance of approximately **O(n log n)** across all input types due to random pivot selection.
- Deterministic Quicksort (pivot = first element) suffers on sorted and reverse-sorted data, showing **O(n²)** behavior.
- Hash Table with Chaining supports efficient insert, search, and delete operations with expected **O(1)** time under uniform hashing assumptions.
- Load factor management and resizing strategies help maintain performance in hash tables.


Conclusion

Randomized algorithms like Quicksort perform reliably under diverse conditions, whereas deterministic strategies may degrade without careful pivot selection. Hash tables, when implemented with chaining and a good hash function, offer robust performance for dictionary-like data operations.


