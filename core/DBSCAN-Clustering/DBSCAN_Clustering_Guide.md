# DBSCAN - Complete Guide

## What is DBSCAN?

DBSCAN stands for Density-Based Spatial Clustering of Applications with Noise.

It groups points based on density instead of distance from centroids.

---

## Core Idea

Dense regions become clusters.

Sparse regions become noise or outliers.

---

## Important Terms

### Core Point
Has at least min_samples neighbors within eps radius.

### Border Point
Close to a core point but lacks enough neighbors.

### Noise Point
Does not belong to any cluster.

---

## Parameters

### eps
Neighborhood radius.

### min_samples
Minimum points required to form a dense region.

---

## Algorithm Steps

1. Select a point.
2. Check neighbors within eps.
3. If neighbors >= min_samples:
   - Create cluster.
4. Expand cluster.
5. Mark remaining isolated points as noise.

---

## Advantages

- No need to specify K.
- Detects outliers automatically.
- Handles irregular cluster shapes.

---

## Limitations

- Sensitive to parameter selection.
- Struggles with varying densities.
- High-dimensional data can be challenging.

---

## Real World Applications

- Fraud Detection
- GPS Route Analysis
- Anomaly Detection
- Image Segmentation
- Network Security

---

## DBSCAN vs K-Means

| Feature | DBSCAN | K-Means |
|----------|---------|----------|
| Need K | No | Yes |
| Outlier Detection | Yes | No |
| Arbitrary Shapes | Yes | No |
| Centroids | No | Yes |

---

## DBSCAN vs Hierarchical

| Feature | DBSCAN | Hierarchical |
|----------|---------|-------------|
| Noise Handling | Excellent | Weak |
| Dendrogram | No | Yes |
| Scalability | Better | Worse |

---

## Interview Questions

1. What are core, border, and noise points?
2. Explain eps and min_samples.
3. Why is DBSCAN good for anomaly detection?
4. DBSCAN vs K-Means?
