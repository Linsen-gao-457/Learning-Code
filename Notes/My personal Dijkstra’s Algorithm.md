# My personal Dijkstra’s Algorithm

[TOC]



## Company Interview Guide

[Guide](https://algo.monster/interview-guides)

## Dijkstra’s Algorithm

High Return on Investment(ROI): DFS, BFS, Two pointers.

Basic data structure and algorithm: Linked List, Array, Hash Map, Stack, Queue, Sorting;Priority Queue/heap has medium ROI

Medium ROI: priority Queue/heap

Low ROI: Greedy, Dynamic Programming

### A Note On Academic Algorithms

A good-enough rule of thumb is an algorithm named after a person(s) you can safely ignore.

Very rarely/almost never used list:

- Minimal spanning tree: Kruskal's algorithm and Prim's algorithm
- Minimum cut: Ford−Fulkerson algorithm
- Shortest path in weight graphs: Bellman−Ford−Moore algorithm
- String search: Boyer−Moore algorithm

Knuth−Morris−Pratt (KMP) algorithm helps solve string problems, but interviewers will NOT expect to know how to do this. Typically bug-free brute force coding is required instead of KMP.

Dijkstra's algorithm helps find the shortest path between nodes in a weighted graph. Weighted graphs interview problems exist but are rare. It's good to have a high-level understanding of this algorithm since it uses a priority queue that frequently gets asked.

[Robin Karp rolling hash algorithm](https://en.wikipedia.org/wiki/Rabin–Karp_algorithm) is sometimes helpful in solving some two-pointer issues.