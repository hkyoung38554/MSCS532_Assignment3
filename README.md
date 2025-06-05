# MSCS532 Assignment3: Understanding Algorithm Efficiency and Scalability

This project implements and analyzes Randomized Quicksort and Hashing with Chaining. It includes both theoretical analysis and practical evaluation to assess the performance, efficiency, and scalability of these algorithms under different input conditions.

## Files

- `randomized_quicksort.py`: Python implementation of Randomized Quicksort with a sample test
- `hash_table.py`: Python implementation of a hash table using chaining for collision resolution
- `Assignment3_Haeri Kyoung.pdf`: Final report containing implementation details, theoretical analysis, empirical results, and conclusion
- `README.md`: Instructions and summary of the project

## How to Run

```bash
python randomized_quicksort.py
python hash_table.py
```

## Summary of Findings

### Randomized Quicksort

- Performed consistently well across various input types including random, sorted, reverse sorted, and repeated-element arrays.
- Maintained an average-case time complexity of order n log n due to balanced partitions created by random pivot selection.
- Avoided worst-case performance seen in deterministic approaches by reducing the chance of unbalanced recursion depth.

### Deterministic Quicksort (Compared in Report)

- Used the first element as the pivot, which led to poor performance on sorted and reverse-sorted inputs.
- Frequently produced unbalanced partitions, increasing the recursion depth and causing runtimes to approach order n squared in the worst case.

### Hash Table with Chaining

- Successfully supported insert, search, and delete operations in expected constant time under simple uniform hashing.
- Demonstrated stable performance as long as the load factor (ratio of elements to slots) remained low.
- Showed how chaining avoids collision overwrites by storing key-value pairs in per-slot lists.
- Highlighted the importance of a good hash function and resizing strategy to ensure performance at scale.

---

This assignment helped reinforce the importance of pivot selection in sorting and the role of hashing strategies in efficient data structure design.
