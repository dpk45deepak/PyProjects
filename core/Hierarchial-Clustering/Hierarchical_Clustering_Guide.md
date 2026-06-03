# Hierarchical Clustering - Complete Guide

## What is Hierarchical Clustering?

Hierarchical Clustering is an unsupervised machine learning algorithm that groups similar data points into clusters and builds a hierarchy of those clusters.

Unlike K-Means, it does not require specifying the number of clusters beforehand.

---

## Types

### 1. Agglomerative (Bottom-Up)
- Start with each point as its own cluster.
- Merge the closest clusters repeatedly.
- Continue until only one cluster remains.

### 2. Divisive (Top-Down)
- Start with one large cluster.
- Split it recursively into smaller clusters.

---

## Key Concept: Dendrogram

A dendrogram is a tree-like diagram that shows how clusters are merged or split.

Benefits:
- Visualizes cluster relationships.
- Helps determine the optimal number of clusters.

---

## Linkage Methods

### Single Linkage
Uses minimum distance between clusters.

### Complete Linkage
Uses maximum distance between clusters.

### Average Linkage
Uses average distance.

### Ward Linkage
Minimizes within-cluster variance.

---

## Algorithm Steps

1. Treat each point as a cluster.
2. Compute distances.
3. Merge nearest clusters.
4. Update distances.
5. Repeat until stopping criterion.

---

## Advantages

- No need to choose K initially.
- Produces dendrogram.
- Good for small datasets.

## Limitations

- Computationally expensive.
- Sensitive to noise.
- Not ideal for huge datasets.

---

## Real World Applications

- Customer Segmentation
- Gene Expression Analysis
- Social Networks
- Document Clustering

---

## Comparison with K-Means

| Feature | Hierarchical | K-Means |
|----------|-------------|----------|
| Need K | No | Yes |
| Dendrogram | Yes | No |
| Speed | Slower | Faster |
| Interpretability | High | Medium |

---

## Interview Questions

1. What is a dendrogram?
2. Difference between agglomerative and divisive?
3. Explain linkage methods.
4. Hierarchical vs K-Means?
