# 📊 Graph in Data Structures (DSA)

## 📌 What is a Graph?

A **Graph** is a data structure used to represent relationships between objects.

A graph is made of:

* **Vertices (Nodes)** → Represent data
* **Edges** → Represent connection between nodes

### 🔹 Simple Diagram

```
    A ------ B
    |        |
    |        |
    D ------ C
```

* A, B, C, D → Nodes (Vertices)
* Lines between them → Edges

---

## 🤔 Why Graph is Used?

Graphs are used when we need to show **connections or relationships**.

### 🔹 Real World Examples

* 🌐 Social Network (Facebook, Instagram)

  * People = Nodes
  * Friendship = Edge

* 🗺️ Google Maps

  * Locations = Nodes
  * Roads = Edges

* ✈️ Flight Routes

  * Cities = Nodes
  * Flights = Edges

* 🧠 Computer Networks

  * Devices = Nodes
  * Connections = Edges

---

## 🧱 Types of Graph (Basic Idea)

* **Directed Graph (Digraph)** → Edges have direction
* **Undirected Graph** → Edges have no direction

Example:

```
A → B (Directed)
A — B (Undirected)
```

---

## 📦 Graph Representation

There are multiple ways to represent a graph in memory.

### 1️⃣ Adjacency Matrix (What you learned)

It is a **2D array (matrix)**.

If there is a connection → 1
If not → 0

### 🔹 Example Graph

```
    A ---- B
    |      |
    D ---- C
```

### 🔹 Matrix Representation

```
    A B C D
A [ 0 1 0 1 ]
B [ 1 0 1 0 ]
C [ 0 1 0 1 ]
D [ 1 0 1 0 ]
```

### ✅ Advantages

* Easy to implement
* Easy to check if edge exists

### ❌ Disadvantages

* Takes more space (n x n)

---

## 📚 Concepts Learned

### ✔️ Graph Basics

* What is node and edge
* How graph works

### ✔️ Adjacency Matrix

* Represent graph using 2D array
* Understand connection using 0 and 1

---

## 🚀 Learning Progress (In Progress)

I am currently learning more concepts in Graph:

### 1️⃣ Adjacency List Representation

* Store graph using list
* Saves space compared to matrix

Example:

```
A → B, D
B → A, C
C → B, D
D → A, C
```

---

### 2️⃣ DFS (Depth First Search)

* Go deep into graph first
* Uses **Stack (or recursion)**

Example Path:

```
A → B → C → D
```

---

### 3️⃣ BFS (Breadth First Search)

* Visit nodes level by level
* Uses **Queue**

Example Path:

```
A → B → D → C
```

---

### 2️⃣ DFS (Depth First Search)

* Go deep into graph first
* Uses **Stack (or recursion)**

Example Path:

```
A → B → C → D
```

---

### 3️⃣ BFS (Breadth First Search)

* Visit nodes level by level
* Uses **Queue**

Example Path:

```
A → B → D → C
```

---

## 🎯 Summary

* Graph is used to represent relationships
* It contains nodes and edges
* You have learned:

  * Graph basics
  * Adjacency Matrix

Currently learning:

* Adjacency List
* DFS
* BFS
* Adjacency List
* DFS
* BFS
